import tkinter
import socket
from threading import Thread


def receive():
    while True:
        try:
            msg = s.recv(1024).decode('utf8')
            if msg == '#quit':
                s.close()
                window.quit()
                break

            msg_list.insert(tkinter.END, msg)
        except Exception as e:
            print("There is an Error Receiving the Message")


def on_send():
    msg = my_msg.get()
    my_msg.set("")
    s.send(bytes(msg, 'utf8'))


def on_closing():
    my_msg.set("#quit")
    on_send()


window = tkinter.Tk()
window.title("Chat Room Application")
window.configure(bg='green')

message_frame = tkinter.Frame(window, height=100, width=100, bg='red')
message_frame.pack()

my_msg = tkinter.StringVar()
my_msg.set("")

scroll_bar = tkinter.Scrollbar(message_frame)
msg_list = tkinter.Listbox(message_frame, height=15, width=100, bg='red', yscrollcommand=scroll_bar.set)
scroll_bar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
scroll_bar.configure(command=msg_list.yview)
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
msg_list.pack()

label = tkinter.Label(window, text="Enter the Message", fg='blue', font='Aeria', bg='red')
label.pack()

entry_field = tkinter.Entry(window, textvariable=my_msg, fg='red', width=50)
entry_field.pack()

send_button = tkinter.Button(window, text="Send", font='Aeria', fg='white', command=on_send)
send_button.pack()

quit_button = tkinter.Button(window, text="Quit", font='Aeria', fg='white', command=on_closing)
quit_button.pack()

HOST = '127.0.0.1'
PORT = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # IPv4, TCP
s.connect((HOST, PORT))

receive_thread = Thread(target=receive)
receive_thread.start()

window.mainloop()
