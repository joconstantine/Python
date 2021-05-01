from tkinter import *
from tkinter import filedialog
import PyPDF2
import pyttsx3
import threading


def extract_text():
    file = filedialog.askopenfile(parent=root, mode='rb',
                                  title="Choose a PDF File")
    if file:
        pdf_reader = PyPDF2.PdfFileReader(file)
        global extracted_text
        extracted_text = ""
        for pageNum in range(pdf_reader.numPages):
            page_object = pdf_reader.getPage(pageNum)
            extracted_text += page_object.extractText()
        file.close()


def speak_text():
    global rate, male, female
    rate = int(rate.get())
    engine.setProperty('rate', rate)
    male = int(male.get())
    female = int(female.get())
    all_voices = engine.getProperty('voices')   # array of all voice types
    male_voice = all_voices[0].id
    female_voice = all_voices[1].id

    if (not male and not female) or (male and female):
        engine.setProperty('voice', male_voice)
    elif female:
        engine.setProperty('voice', female_voice)
    else:
        engine.setProperty('voice', male)

        engine.say(extracted_text)
        engine.runAndWait()


def stop_speaking():
    engine.stop()


def application(root_input: Tk):
    root_input.geometry('{}x{}'.format(700, 600))  # 700x600
    root_input.resizable(width=False, height=False)  # disabling resizing
    root_input.title("PDF to AUDIO")
    root_input.configure(background='light grey')
    global rate, male, female

    # frame1
    frame1 = Frame(root_input, width=500, height=200, bg='indigo')
    # frame2
    frame2 = Frame(root_input, width=500, height=450, bg='light grey')
    frame1.pack(side='top', fill='both')  # fill both 4 directions
    frame2.pack(side='top', fill='y')  # fill only the y axis

    # frame1 Widgets
    name1 = Label(frame1, text="PDF to AUDIO", fg='black', bg='blue',
                  font=('Arial', 28, 'bold'))
    name1.pack()

    name2 = Label(frame1, text="Hear your PDF File", fg='red', bg='indigo',
                  font=('Calibre', 25, 'bold'))
    name2.pack()

    # frame 2 widgets
    btn = Button(frame2, text="Select PDF File", activeforeground='red',
                 command=extract_text, padx='70', pady='10',
                 fg='white', bg='black', font=('Arial', 12))
    btn.grid(row=0, pady=20, columnspan=2)

    rate_text = Label(frame2, text="Enter Rate of Speech:", fg='black', bg='aqua',
                      font=('Arial', 12))
    rate_text.grid(row=1, column=0, pady=15, padx=0, sticky=E)
    rate = Entry(frame2, fg='black', bg='white', font=('Arial', 12))
    rate.grid(row=1, column=1, padx=30, pady=15, sticky=W)

    voice_text = Label(frame2, text="Select Voice:", fg='black', bg='aqua',
                       font=('Arial', 12))
    voice_text.grid(row=2, column=0, pady=15, padx=0, sticky=E)
    male = IntVar()
    male_opt = Checkbutton(frame2, text="Male", bg='pink', variable=male,
                           onvalue=1, offvalue=0)
    male_opt.grid(row=2, column=1, pady=0, padx=30, sticky=W)

    female = IntVar()
    female_opt = Checkbutton(frame2, text="Female", bg='pink', variable=female,
                             onvalue=1, offvalue=0)
    female_opt.grid(row=3, column=1, pady=0, padx=30, sticky=W)

    submit_btn = Button(frame2, text="Play PDF File", command=speak_text,
                        activeforeground='red', padx=60, pady=10,
                        fg='white', bg='black', font=('Arial', 12))
    submit_btn.grid(row=4, column=0, pady=65)

    stop_btn = Button(frame2, text="Stop Playing", command=stop_speaking,
                      activeforeground='red', padx=60, pady=10, fg='white',
                      bg='black', font=('Arial', 12))
    stop_btn.grid(row=4, column=1, pady=65)


if __name__ == '__main__':
    extracted_text, rate, male, female = "", 100, 0, 0
    engine = pyttsx3.init()
    root = Tk()
    application(root)
    root.mainloop()
