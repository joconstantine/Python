import tkinter as tk

Keyboard_App = tk.Tk()

keys = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '=',
        'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'DEL',
        'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', '"',
        'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '!', 'TAB',
        'SPACE']

curBut = [-1, -1]
buttonL = [[]]
entry = tk.Text(Keyboard_App, width=97, height=8)
entry.grid(row=0, columnspan=15)

varRow = 1
varColumn = 0


def leftKey(_=None):
    if curBut == [-1, -1]:
        curBut[:] = [0, 0]
        buttonL[0][0].configure(highlightbackground="red")
    elif curBut[0] == 4:  # Space button
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground="red")
        curBut[:] = [0, 10]  # moving to the "=" button
        buttonL[0][10].configure(highlightbackground="red")
    else:
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground="red")
        curBut[:] = [curBut[0], (curBut[1] - 1) % 11]  # to wrap around if needed
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground="red")

    buttonL[curBut[0]][curBut[1]].focus_set()


def rightKey(_=None):
    if curBut == [-1, -1]:
        curBut[:] = [0, 0]
        buttonL[0][0].configure(highlightbackground="red")
    elif curBut[0] == 4:  # Space button
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground="red")
        curBut[:] = [0, 0]  # moving to the "1" button
        buttonL[0][10].configure(highlightbackground="red")
    else:
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground="red")
        curBut[:] = [curBut[0], (curBut[1] + 1) % 11]  # to wrap around if needed
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground="red")

    buttonL[curBut[0]][curBut[1]].focus_set()


def upKey(_=None):
    if curBut == [-1, -1]:
        curBut[:] = [0, 0]
        buttonL[0][0].configure(highlightbackground="red")
    elif curBut[0] == 0:  # first row
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground="red")
        curBut[:] = [(curBut[0] - 1) % 5, 0]  # Space button
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground="red")
    elif curBut[0] == 4:  # Space button
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground="red")
        curBut[:] = [(curBut[0] - 1) % 5, 5]
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground="red")
    else:
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground="red")
        curBut[:] = [(curBut[0] - 1) % 5, curBut[1]]  # to wrap around if needed
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground="red")

    buttonL[curBut[0]][curBut[1]].focus_set()


def downKey(_=None):
    if curBut == [-1, -1]:
        curBut[:] = [0, 0]
        buttonL[0][0].configure(highlightbackground="red")
    elif curBut[0] == 3:  # second last row
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground="red")
        curBut[:] = [(curBut[0] + 1) % 5, 0]  # Space button
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground="red")
    elif curBut[0] == 4:  # Space button
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground="red")
        curBut[:] = [(curBut[0] + 1) % 5, 5]
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground="red")
    else:
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground="red")
        curBut[:] = [(curBut[0] + 1) % 5, curBut[1]]  # to wrap around if needed
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground="red")

    buttonL[curBut[0]][curBut[1]].focus_set()


def select(value, x, y):
    if curBut != [-1, -1]:  # unhighlight the previously-clicked button
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground="red")
        buttonL[curBut[0]][curBut[1]].configure(highlightcolor="red")
    curBut[:] = [x, y]

    # highlight the clicked button
    buttonL[x][y].configure(highlightbackground="red")
    buttonL[x][y].configure(highlightcolor="red")

    if value == 'DEL':
        input_val = entry.get("1.0", "end-2c")
        entry.delete("1.0", "end")
        entry.insert("1.0", input_val, "end")
    elif value == 'SPACE':
        entry.insert("insert", " ")
    elif value == 'TAB':
        entry.insert("insert", "\t")
    else:
        entry.insert("insert", value)


for button in keys:
    if button != 'SPACE':
        but = tk.Button(Keyboard_App, text=button, width=5, bg="black", fg="white",
                        highlightthickness=4, activebackground="gray",
                        activeforeground="red", highlightcolor="red", relief="raised",
                        padx=12, pady=4, bd=4, command=lambda x=button, i=varRow - 1,
                                                              j=varColumn: select(x, i, j))
        but.bind('<Return>', lambda x=button, i=varRow - 1,
                                    j=varColumn: select(x, i, j))
        buttonL[varRow - 1].append(but)
        but.grid(row=varRow, column=varColumn)
    else:
        but = tk.Button(Keyboard_App, text=button, width=60, bg="black", fg="white",
                        highlightthickness=4, activebackground="gray65",
                        activeforeground="red", highlightcolor="red", relief="raised",
                        padx=4, pady=4, bd=4, command=lambda x=button, i=varRow - 1,
                                                             j=varColumn: select(x, i, j))
        but.bind('<Return>', lambda x=button, i=varRow - 1,
                                    j=varColumn: select(x, i, j))
        buttonL[varRow - 1].append(but)
        but.grid(row=6, columnspan=16)

    varColumn += 1
    if varColumn > 10:
        varColumn = 0
        varRow += 1
        buttonL.append([])

Keyboard_App.bind('<Left>', leftKey)
Keyboard_App.bind('<Right>', rightKey)
Keyboard_App.bind('<Up>', upKey)
Keyboard_App.bind('<Down>', downKey)

Keyboard_App.mainloop()
