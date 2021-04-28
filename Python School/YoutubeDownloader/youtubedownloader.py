from pytube import YouTube
from tkinter import filedialog
from tkinter import ttk
import tkinter
import re
import threading


class Application:
    def __init__(self, root: tkinter.Tk):
        self.root = root
        self.newWindow = None
        self.root.grid_rowconfigure(0, weight=2)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.config(bg='#ffdddd')

        top_label = tkinter.Label(self.root, text="YouTube Download Manager", fg='orange',
                                  font=('.VnArabia', 70))
        top_label.grid(pady=(0, 10))

        link_label = tkinter.Label(self.root, text="Please paste any YouTube video link below",
                                   font=('SnowPersons', 30))
        link_label.grid(pady=(0, 20))

        self.youtubeEntryVar = tkinter.StringVar()

        self.youtubeEntry = tkinter.Entry(self.root, width=70, textvariable=self.youtubeEntryVar,
                                          font=(".VnAristote", 25))
        self.youtubeEntry.grid(pady=(0, 15), ipady=2)

        self.youtubeEntryError = tkinter.Label(self.root, text="")
        self.youtubeEntryError.grid(pady=(0, 8))

        self.youtubeFileSaveLabel = tkinter.Label(self.root, text="Choose Directory", font=(".VnBodoni", 30))
        self.youtubeFileSaveLabel.grid()

        self.youtubeFileDirectoryButton = tkinter.Button(self.root, text="Directory", font=("Bell MT", 15),
                                                         command=self.open_directory)
        self.youtubeFileDirectoryButton.grid(pady=(10, 3))

        self.fileLocationLabel = tkinter.Label(self.root, text="", font=("Freestyle Script", 25))
        self.fileLocationLabel.grid()
        self.FolderName = None
        self.matchYoutubeLink = None

        self.youtubeChooseLabel = tkinter.Label(self.root, text="Choose the Download Type", font=("Variety", 30))
        self.youtubeChooseLabel.grid()

        self.downloadChoices = [("Audio MP3", 1), ("Video MP4", 2)]

        self.choicesVar = tkinter.StringVar()
        self.choicesVar.set(1)  # default value = 1 - Audio MP3

        for text, mode in self.downloadChoices:
            self.youtubeChoices = tkinter.Radiobutton(self.root, text=text, font=("Northwest old", 15),
                                                      variable=self.choicesVar, value=mode)
            self.youtubeChoices.grid()

        self.downloadButton = tkinter.Button(self.root, text="Download", width=10, font=("Bell MT", 15),
                                             command=self.check_youtube_link)
        self.downloadButton.grid(pady=(30, 5))

    def open_directory(self):
        self.FolderName = filedialog.askdirectory()

        if len(self.FolderName) > 0:
            self.fileLocationLabel.config(text=self.FolderName, fg='green')
            return True
        else:
            self.fileLocationLabel.config(text="Please choose a Directory", fg='red')
            return False

    def check_youtube_link(self):
        self.matchYoutubeLink = re.match("^https://www.youtube.com/.", self.youtubeEntryVar.get())
        if not self.matchYoutubeLink:
            self.youtubeEntryError.config(text="Invalid YouTube Link", fg='red')
        elif not self.open_directory():
            self.fileLocationLabel.config(text="Please choose a Directory", fg='red')
        elif self.matchYoutubeLink and self.fileLocationLabel:
            self.download_window()

    def download_window(self):
        self.newWindow = tkinter.Toplevel(self.root)
        self.root.withdraw()


if __name__ == '__main__':
    window = tkinter.Tk()
    window.title("YouTube Download Manager")
    window.state("zoomed")

    app = Application(window)

    window.mainloop()
