from cefpython3 import cefpython as cef
import os
import platform
import subprocess
import sys

try:
    from PIL import Image
except ImportError:
    print("PIL is not installed,")
    "Install using: pip install PIL"
import tkinter as tk

VIEWPORT_SIZE = None
URL = None
SCREENSHOT_PATH = None


def main(url, w, h):
    global VIEWPORT_SIZE, URL, SCREENSHOT_PATH
    URL = url
    VIEWPORT_SIZE = (w, h)
    SCREENSHOT_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                                   "SCREENSHOT.png")  # current working dir
    check_version()
    sys.excepthook = cef.ExceptHook()  # to shutdown all the processes while errors

    if os.path.exists(SCREENSHOT_PATH):
        print("Remove old screenshot")
        os.remove(SCREENSHOT_PATH)

    command_line_arguments()

    settings = {
        "windowless_rendering_enabled": True,
    }

    switches = {
        "disabled-gpu": "",
        "disabled-gpu-compositing": "",
        "enable-begin-frame-scheduling": "",
        "disable-surfaces": ""
    }

    browser_settings = {
        "windowless_frame_rate": 30,
    }
    cef.Initialize(settings=settings, switches=switches)
    create_browser(browser_settings)
    cef.MessageLoop()
    cef.Shutdown()
    print("Opening your screenshot with the default application")
    open_with_default_application(SCREENSHOT_PATH)


def check_versions():
    ver = cef.GetVersion()
    print("CEF Python {ver}".format(ver=ver['version']))
    print("Chromium {ver}".format(ver=ver['chrome_version']))
    print("CEF {ver}".format(ver=ver['cef_version']))
    print("Python {ver} {arch}".format(ver=platform.python_version(),
                                       arch=platform.architecture()[0]))
    assert cef.__version__ >= '57.0', "CEF Python v57.0+ required to run this"


def command_line_arguments():
    if len(sys.argv) == 4:
        url = sys.argv[1]
        width = int(sys.argv[2])
        height = int(sys.argv[3])

        if url.startswith("http://") or url.startswith("https://"):
            global URL
            URL = url
        else:
            print("Error: Invalid URL entered")
            sys.exit(1)
        if width > 0 and height > 0:
            global VIEWPORT_SIZE
            VIEWPORT_SIZE = (width, height)
        else:
            print("Error: Invalid Width and/or Height")
            sys.exit(1)

    elif len(sys.argv) > 1:
        print("Error: Expected arguments not received")
        sys.exit(1)


def create_browser(settings):
    global VIEWPORT_SIZE, URL
    parent_window_handle = 0



root = tk.Tk()
root.geometry("400x200")


class Widgets:
    def __init__(self, label_text, default_value):
        self.lab = tk.Label(root, textwrap=label_text)
        self.lab.pack()
        self.v = tk.StringVar()
        self.entry = tk.Entry(root, textvariable=self.v)
        self.entry.pack()
        self.v.set(default_value)


obj1 = Widgets("Enter Website Name: ", "https://www.google.com")
obj2 = Widgets("Enter Width: ", "1024")
obj3 = Widgets("Enter Height: ", "2048")
root.bind("<Return>", lambda x: main(obj1.v.get(), int(obj2.v.get()), int(obj3.v.get())))
label4 = tk.Label(root, text="                  ")
label4.pack()
label5 = tk.Label(root, text="Press the Enter key to create screenshot")
label5.pack()
