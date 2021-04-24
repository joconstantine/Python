import tkinter
import smtplib
import re

username = ""
password = ""
server = smtplib.SMTP('smtp.gmail.com:587')


def login():
    if validate_login():
        try:
            global username
            global password
            username = str(entry1.get())  # username is from entry1
            password = str(entry2.get())  # password is from entry 2
            global server
            server.ehlo()
            server.starttls()   # upgrade unsecured SMTP connection to secured
            server.login(username, password)
            f2.pack()
            btn2.grid()
            label4['text'] = "Logged In!"
            root.after(10, root.grid)   # call root.grid after 10 milliseconds
            f1.pack_forget()    # destroy all widgets associated with f1
            root.after(10, root.grid)
            f3.pack()
            label9.grid_remove()
            root.after(10, root.grid)
        except smtplib.SMTPAuthenticationError:
            f2.pack()
            label4.grid()
            label4['text'] = "Invalid Credentials!"
            btn2.grid_remove()
            root.after(10, root.grid)


def hide_login_label():
    f2.pack_forget()  # f2 was packed, so to use pack_forget
    f3.pack_forget()  # f3 was packed, so to use pack_forget
    root.after(10, root.grid)


def send_mail():
    if validate_message():
        label9.grid_remove()
        root.after(10, root.grid)
        receiver = str(entry3.get())
        subject = str(entry4.get())
        msg_body = str(entry5.get())
        msg = "From: " + username + "\n" + "To: " + receiver + "\n" + "Subject: " \
              + subject + "\n" + msg_body
        try:
            server.sendmail(username, receiver, msg)
            label9.grid()
            label9['text'] = "Mail Sent!"
            root.after(10, root.grid)
        except Exception as e:
            label9.grid()
            label9['text'] = "Error in Sending Your Email"
            root.after(10, root.grid)


def logout():
    try:
        server.quit()
        f3.pack_forget()
        f2.pack()
        label4.grid()
        label4['text'] = "Logged Out Successfully!"
        btn2.grid_remove()
        entry2.delete(0, tkinter.END)
        root.after(10, root.grid)
    except Exception as e:
        label4['text'] = "Error in Logout!"


def validate_login():
    email_text = str(entry1.get())
    pass_text = str(entry2.get())
    if (email_text == "") or (pass_text == ""):
        f2.pack()
        label4.grid()
        label4['text'] = "Fill all the Fields!"
        btn2.grid_remove()
        root.after(10, root.grid)
        return False
    else:
        EMAIL_REGEX = re.compile(r"[^@\s]+@[^@\s]+\.[a-zA-Z0-9]+$")
        if not EMAIL_REGEX.match(email_text):
            f2.pack()
            label4.grid()
            label4['text'] = "Enter a valid Email Address!"
            btn2.grid_remove()
            root.after(10, root.grid)
            return False
        else:
            return True


def validate_message():
    receiver_text = str(entry3.get())
    sub_text = str(entry4.get())
    msg_text = str(entry5.get())

    if (receiver_text == "") or (sub_text == "") or (msg_text == ""):
        label9.grid()
        label9['text'] = "Fill in all the Places!"
        root.after(10, root.grid)
        return False
    else:
        EMAIL_REGEX = re.compile(r"[^@\s]+@[^@\s]+\.[a-zA-Z0-9]+$")
        if not EMAIL_REGEX.match(receiver_text):
            label9.grid()
            label9['text'] = "Enter a valid Email Address!"
            root.after(10, root.grid)
            return False
        elif (len(sub_text) < 3) or (len(msg_text) < 3):
            label9.grid()
            label9['text'] = "Enter at least 3 characters!"
            root.after(10, root.grid)
            return False
        else:
            return True


root = tkinter.Tk()
root.title("Email Application")

f1 = tkinter.Frame(root, width=1000, height=800)
f1.pack(side=tkinter.TOP)

label1 = tkinter.Label(f1, width=25, text="Enter your Credentials", font=('Calibri 18 bold'))
label1.grid(row=0, columnspan=3, pady=10, padx=10)

label2 = tkinter.Label(f1, text="Email").grid(row=1, sticky=tkinter.E, pady=5, padx=10)
label3 = tkinter.Label(f1, text="Password").grid(row=2, sticky=tkinter.E, pady=5, padx=10)

entry1 = tkinter.Entry(f1)
entry2 = tkinter.Entry(f1, show='*')    # show * instead of the actual input value

entry1.grid(row=1, column=1, pady=5)
entry2.grid(row=2, column=1)

btn1 = tkinter.Button(f1, text="Login", width=10, bg='black', fg='white', command=lambda: login())
btn1.grid(row=3, columnspan=3, pady=10)

f2 = tkinter.Frame(root)
f2.pack(side=tkinter.TOP, expand=tkinter.YES, fill=tkinter.NONE)

label4 = tkinter.Label(f2, width=20, bg='cyan', fg='red', text="Logged in!", font=('Calibri 12 bold'), wraplength=100)
label4.grid(row=0, column=0, columnspan=2, pady=5)

btn2 = tkinter.Button(f2, text="Logout", bg='black', fg='white', command=lambda: logout())
btn2.grid(row=0, column=4, sticky=tkinter.E, pady=10, padx=50)


f3 = tkinter.Frame(master=root)  # tkinter.Frame(root)
f3.pack(side=tkinter.TOP, expand=tkinter.NO, fill=tkinter.NONE)

label5 = tkinter.Label(f3, width=20, text="Compose Email", font=('Calibri 18 bold'))
label5.grid(row=0, columnspan=3, pady=10)

label6 = tkinter.Label(f3, text="To").grid(row=1, sticky=tkinter.E, pady=5)
label7 = tkinter.Label(f3, text="Subject").grid(row=2, sticky=tkinter.E)
label8 = tkinter.Label(f3, text="Message").grid(row=3, sticky=tkinter.E)

entry3 = tkinter.Entry(f3)
entry4 = tkinter.Entry(f3)
entry5 = tkinter.Entry(f3)

entry3.grid(row=1, column=1, pady=5)
entry4.grid(row=2, column=1, pady=5)
entry5.grid(row=3, column=1, pady=5, rowspan=3)

btn3 = tkinter.Button(f3, text="Send Mail", width=10, bg='black', fg='white',
                      command=lambda: send_mail())
btn3.grid(row=6, columnspan=3, pady=10)

label9 = tkinter.Label(f3, width=20, fg='white', bg='black', font=('Calibri 18 bold'))
label9.grid(row=7, columnspan=3, pady=5)

hide_login_label()

root.mainloop()
