# Write a GUI program to create a simple calculator
# layout that looks like the screenshot.
#
# Try to be as Pythonic as possible - it's ok if you
# end up writing repeated Button and Grid statements,
# but consider using lists and a for loop.
#
# There is no need to store the buttons in variables.
#
# As an optional extra, refer to the documentation to
# work out how to use minsize() to prevent your window
# from being shrunk so that the widgets vanish from view.
#
# Hint: You may want to use the widgets .winfo_height() and
# winfo_width() methods, in which case you should know that
# they will not return the correct results unless the window
# has been forced to draw the widgets by calling its .update()
# method first.
#
# If you are using Windows you will probably find that the
# width is already constrained and can't be resized too small.
# The height will still need to be constrained, though.

import tkinter

mainWindow = tkinter.Tk()

mainWindow.title("Calculator")
mainWindow.geometry('640x470+200-200')
mainWindow['padx'] = 8

mainWindow.columnconfigure(0, weight=10)
mainWindow.columnconfigure(1, weight=12)
mainWindow.columnconfigure(2, weight=10)
mainWindow.columnconfigure(3, weight=10)
mainWindow.columnconfigure(4, weight=2)
mainWindow.columnconfigure(5, weight=20)
mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=2)
mainWindow.rowconfigure(2, weight=2)
mainWindow.rowconfigure(3, weight=2)
mainWindow.rowconfigure(4, weight=2)
mainWindow.rowconfigure(5, weight=2)
mainWindow.rowconfigure(6, weight=4)

result = tkinter.Entry(mainWindow)
result.grid(row=0, column=0, columnspan=5, sticky='nsew')

c_button = tkinter.Button(mainWindow, text="C")
c_button.grid(row=1, column=0, sticky='nsew')

ce_button = tkinter.Button(mainWindow, text="CE")
ce_button.grid(row=1, column=1, sticky='nsew')

for i in range(1, 10):
    num_button = tkinter.Button(mainWindow, text=i)
    num_button.grid(row=((i - 1) // 3 + 2), column=((i - 1) % 3), sticky='nsew')

plus_button = tkinter.Button(mainWindow, text="+")
plus_button.grid(row=2, column=3, sticky='nsew')

minus_button = tkinter.Button(mainWindow, text="-")
minus_button.grid(row=3, column=3, sticky='nsew')

multiply_button = tkinter.Button(mainWindow, text="*")
multiply_button.grid(row=4, column=3, sticky='nsew')

zero_button = tkinter.Button(mainWindow, text="0")
zero_button.grid(row=5, column=0, sticky='nsew')

equal_button = tkinter.Button(mainWindow, text="=")
equal_button.grid(row=5, column=1, columnspan=2, sticky='nsew')

divide_button = tkinter.Button(mainWindow, text="/")
divide_button.grid(row=5, column=3, sticky='nsew')

mainWindow.update()
mainWindow.minsize()

mainWindow.mainloop()
