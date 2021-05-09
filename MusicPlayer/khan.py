from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
from pygame import mixer
import tkinter.messagebox

window = Tk()
mixer.init()

window.geometry('300x300')
window.title('Python Music Player')
filename = ""
paused = False


def browse_file():
    global filename
    filename = filedialog.askopenfilename()


def help_me():
    tkinter.messagebox.showinfo(title="Hi!", message="Trung loves Huy")


menu_bar = Menu(window)
sub_menu = Menu(menu_bar, tearoff=False)
window.config(menu=menu_bar)

menu_bar.add_cascade(label="File", menu=sub_menu)
sub_menu.add_command(label="Open", command=browse_file)
sub_menu.add_command(label="Exit", command=window.destroy)

sub_menu = Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="About Us", menu=sub_menu)
sub_menu.add_command(label="Help", command=help_me)

textLabel = Label(window, text="This is a Play Button")
textLabel.pack()


def play_music():
    try:
        mixer.music.load(filename)
        mixer.music.set_volume(0.5)
        mixer.music.play()
        global paused
        paused = False
        pauseButton.config(text="PAUSE")
        statusBar['text'] = "Music is playing"
    except:
        tkinter.messagebox.showerror(title="Error", message="Error in playing the music!")


def stop_music():
    mixer.music.stop()
    statusBar['text'] = "Music is stopped"


def set_volume(value):
    volume = int(value) / 100  # range of volume is between 0 and 1
    mixer.music.set_volume(volume)


def pause_music():
    global paused
    if not paused:
        mixer.music.pause()
        pauseButton.config(text="PLAY")
        statusBar['text'] = "Music is paused"
    else:
        mixer.music.unpause()
        pauseButton.config(text="PAUSE")
        statusBar['text'] = "Music is resumed"
    paused = not paused


def rewind_music():
    mixer.music.rewind()
    statusBar['text'] = "Music is rewinded"


frame = Frame(window)
frame.pack(padx=10, pady=10)


photo = ImageTk.PhotoImage(Image.open("play.jpeg"))  # PIL solution
playButton = Button(frame, image=photo, height=15, width=45, command=play_music)
playButton.grid(row=0, column=0, padx=10)

stopButton = Button(frame, text="STOP", command=stop_music)
stopButton.grid(row=0, column=1, padx=10)

pauseButton = Button(frame, text="PAUSE", command=pause_music)
pauseButton.grid(row=0, column=2, padx=10)

bottomFrame = Frame(window)
bottomFrame.pack()

rewindButton = Button(bottomFrame, text="REWIND", command=rewind_music)
rewindButton.grid(row=0, column=0)

scale = Scale(bottomFrame, from_=0, to=100, orient=HORIZONTAL, command=set_volume)
scale.set(50)
scale.grid(row=0, column=1, padx=10)

statusBar = Label(window, text="Keep enjoying the music", relief=SUNKEN, anchor=W)
statusBar.pack(side=BOTTOM, fill=X)

window.mainloop()
