import tkinter as tk


class TICTACTOE(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tic Tac Toe")
        self.buttons = []
        self.turn = True
        self.count = 0
        self.resizable(width=False, height=False)
        self.board()

    def board(self):
        for i in range(0, 3):
            row = []
            for j in range(0, 3):
                row.append(tk.Button(self, width=8, height=2, font="Calibre 35 bold",
                                     command=lambda x=i, y=j: self.turn_taken(x, y)))
                row[j].grid(row=i, column=j)
            self.buttons.append(row)
        tk.Button(self, text="New Game", width=10, height=1, font="Calibre 15 bold",
                  bg='black', fg='white', activebackground='blue3', activeforeground='white',
                  command=self.new_game).grid(row=3, column=1)

    def turn_taken(self, x, y):
        self.count += 1
        if self.turn:
            char = 'X'
            self.buttons[x][y].configure(text='X', bg='black', state=tk.DISABLED)
        else:
            char = 'O'
            self.buttons[x][y].configure(text='O', bg='white', state=tk.DISABLED)
        self.check_results(char)
        self.turn = not self.turn

    def new_game(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.buttons = []
        self.turn = True
        self.count = 0
        self.board()

    def check_results(self, c):
        if (((self.buttons[0][0]["text"] == c) and (self.buttons[0][1]["text"] == c)
             and (self.buttons[0][2]["text"] == c)) or
                ((self.buttons[1][0]["text"] == c) and (self.buttons[1][1]["text"] == c)
                 and (self.buttons[1][2]["text"] == c)) or
                ((self.buttons[2][0]["text"] == c) and (self.buttons[2][1]["text"] == c)
                 and (self.buttons[2][2]["text"] == c)) or
                ((self.buttons[0][0]["text"] == c) and (self.buttons[1][0]["text"] == c)
                 and (self.buttons[2][0]["text"] == c)) or
                ((self.buttons[0][1]["text"] == c) and (self.buttons[1][1]["text"] == c)
                 and (self.buttons[2][1]["text"] == c)) or
                ((self.buttons[0][2]["text"] == c) and (self.buttons[1][2]["text"] == c)
                 and (self.buttons[2][2]["text"] == c)) or
                ((self.buttons[0][0]["text"] == c) and (self.buttons[1][1]["text"] == c)
                 and (self.buttons[2][2]["text"] == c)) or
                ((self.buttons[0][2]["text"] == c) and (self.buttons[1][1]["text"] == c)
                 and (self.buttons[2][0]["text"] == c))):
            self.result(c)
        elif self.count == 9:
            self.result("Draw")

    def result(self, char):
        top = tk.Toplevel(self)
        if char == "Draw":
            top.title("OOPS!")
            top_text = tk.Label(top, text=f"It is a draw!", font="Calibre 30 bold", fg="blue")
        else:
            top.title("Congratulations!")
            top_text = tk.Label(top, text=f"{char} is a winner", font="Calibre 30 bold",
                                fg="blue")

        top_button = tk.Button(top, text="New Game", bg="black", fg="white",
                               activebackground="blue3", activeforeground="white",
                               command=self.new_game)
        top_text.grid(row=0, column=0, padx=10, pady=10)
        top_button.grid(row=1, column=0)


TICTACTOE().mainloop()
