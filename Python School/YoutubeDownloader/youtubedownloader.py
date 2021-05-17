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
        self.app = None

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
        elif not self.FolderName:
            self.fileLocationLabel.config(text="Please choose a Directory", fg='red')
        elif self.matchYoutubeLink and self.FolderName:
            self.download_window()

    def download_window(self):
        self.newWindow = tkinter.Toplevel(self.root)
        self.root.withdraw()
        self.newWindow.state('zoomed')
        self.newWindow.grid_rowconfigure(0, weight=0)
        self.newWindow.grid_columnconfigure(0, weight=1)

        self.app = SecondApp(self.newWindow, self.youtubeEntryVar.get(), self.FolderName, self.choicesVar.get())


class SecondApp:
    def __init__(self, download_window, youtube_link, folder_name, choices):
        self.downloadWindow = download_window
        self.youtubeLink = youtube_link
        self.folderName = folder_name
        self.choices = choices
        self.percentCount = 0
        self.downloadFinished = None
        self.downloadFileName = None
        self.downloadFileSize = None

        self.yt = YouTube(self.youtubeLink)

        if choices == "1":  # 1 - audio part
            self.video_type = self.yt.streams.filter(only_audio=True).first()  # to download the first audio type
            self.maxFileSize = self.video_type.filesize  # max size of the file
        elif choices == "2":  # 2 - video as well
            self.video_type = self.yt.streams.get_highest_resolution()  # to download the first video format (e.g. 1080px)
            self.maxFileSize = self.video_type.filesize

        self.loadingLabel = tkinter.Label(self.downloadWindow, text="Downloading in Progress", font=("Small Fonts", 40))
        self.loadingLabel.grid(pady=(100, 0))

        self.loadingPercent = tkinter.Label(self.downloadWindow, text="0", fg='green', font=("Agency Fb", 40))
        self.loadingPercent.grid(pady=(50, 0))

        self.progressBar = ttk.Progressbar(self.downloadWindow, length=500, orient='horizontal', mode='indeterminate')
        self.progressBar.grid(pady=(50, 0))
        self.progressBar.start()

        # Thread to keep track of progress
        threading.Thread(target=self.yt.register_on_progress_callback(self.show_progress)).start()

        # Thread to download the file
        threading.Thread(target=self.download_file).start()

    def download_file(self):
        if self.choices == "1":
            self.yt.streams.filter(only_audio=True).first().download(self.folderName)
        elif self.choices == "2":
            self.yt.streams.get_highest_resolution().download(self.folderName)

    def show_progress(self, stream=None, chunk=None, bytes_remaining=None):
        self.percentCount = float("%0.2f" % (100 - (100 * (bytes_remaining / self.maxFileSize))))
        self.loadingPercent.config(text=self.percentCount)

        if self.percentCount < 100:
            pass
        else:
            self.progressBar.stop()
            self.loadingLabel.grid_forget()
            self.progressBar.grid_forget()

            self.downloadFinished = tkinter.Label(self.downloadWindow, text="Download Finished")
            self.downloadFinished.grid(pady=(150, 0))

            self.downloadFileName = tkinter.Label(self.downloadWindow, text=self.yt.title, font=("Terminal", 30))
            self.downloadFileName.grid(pady=(50, 0))

            MB = float("%0.2f" % (self.maxFileSize / 1000000))
            self.downloadFileSize = tkinter.Label(self.downloadWindow, text=str(MB), font=("Agency Fb", 30))
            self.downloadFileSize.grid(pady=(50, 0))


if __name__ == '__main__':
    window = tkinter.Tk()
    window.title("YouTube Download Manager")
    window.state("zoomed")

    app = Application(window)

    window.mainloop()
