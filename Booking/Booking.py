import tkinter
import tkinter as tk
import tkinter.ttk

screens = ["Screen 1", "Screen 2", "Screen 3", "Screen 4", "Screen 5", "Screen 6"]

movies = {"Horror": ["Hereditary", "A Quiet Place", "The Conjuring 2", "The Grudge",
                     "Annabelle Comes Home"],
          "Action": ["Avengers End Game", "John Wick Chapter 3", "Aquaman", "Black Panther",
                     "Mission Impossible"],
          "Drama": ["Joker", "Spotlight", "Little Women", "The Irishman", "A Star Is Born"],
          "Comedy": ["Step Brothers", "Booksmart", "Horrible Bosses", "The Other Guys",
                     "Superbad"],
          "Sci-Fi": ["Star Wars", "Annihilation", "Arrival", "Interstellar", "The Martian"],
          "Romance": ["The Fault in our Stars", "The Notebook", "The Tourist", "Titanic",
                      "Crazy Rich Asians"],
          }

times = ["10:00", "10:30", "11:00", "11:30", "12:00", "12:30", "13:00", "13:30",
         "14:00", "14:30", "15:00", "15:30", "16:00", "16:30"]

seatList = []
seatSelected = []


class Application(tk.Tk):  # extends Tk class
    def __init__(self):
        super().__init__()
        self.title("Cinema Booking")
        self.create_widgets()

    def update_movies(self, event=None):
        self.movie_combo['values'] = movies[self.genre_combo.get()]

    def create_widgets(self, event=None):
        heading_label = tk.Label(self, text="Cinema Seat Booking",
                                 font="Aries 12 bold")
        heading_label.grid(row=0, column=0, columnspan=5, padx=10, pady=10, sticky=tk.W)
        tkinter.ttk.Separator(self, orient=tk.HORIZONTAL).grid(row=1, column=0,
                                                               columnspan=5, sticky=tk.EW)
        day = tk.Frame(self)
        tk.Label(day, text="_______").pack()
        tk.Label(day, text="Today", font="Aries 10 underline").pack()
        tk.Label(day, text="").pack()
        day.grid(row=2, column=0, padx=10)

        tk.Label(self, text="Genre: ").grid(row=2, column=1, padx=(10, 0))
        self.genre_combo = tkinter.ttk.Combobox(self, width=15, values=list(movies.keys()),
                                                state="readony")
        self.genre_combo.set("Select Genre")
        self.genre_combo.bind('<<ComboboxSelected>>', self.update_movies)
        self.genre_combo.grid(row=2, column=2)
        tk.Label(self, text="Movie: ").grid(row=2, column=3, padx=(10, 0))

        self.movie_combo = tkinter.ttk.Combobox(self, width=15, state="readonly")
        self.movie_combo.bind('<<ComboboxSelected>>', self.create_time_buttons)
        self.movie_combo.set("Select Movie")
        self.movie_combo.grid(row=2, column=4, padx=(10, 0))
        tkinter.ttk.Separator(self, orient=tk.HORIZONTAL).grid(row=3, column=0,
                                                               columnspan=5, sticky=tk.EW)

    def create_time_buttons(self, event=None):
        tk.Label(self, text="Select Time Slot", font="Aries 11 bold underline").grid(
            row=4, column=2, columnspan=2, pady=5
        )
        Time = tk.Frame(self)
        Time.grid(row=5, column=0, columnspan=5)
        for i in range(len(times)):
            tk.Button(Time, text=times[i], command=self.seat_selection).grid(row=(i // 7),
                                                                             column=(i % 7))

    def seat_selection(self):
        window = tk.Toplevel()
        window.title("Select your seat")
        checkout_heading = tk.Label(window, text="Seat(s) selection", font="Aries 12")
        checkout_heading.grid(row=0, column=0, columnspan=5, padx=10, pady=(10, 0), sticky=tk.W)

        infer = tk.Frame(window)
        infer.grid(row=1, column=0)
        tk.Label(infer, text="BLUE = SELECTED", fg='blue').grid(row=0, column=0, padx=10)
        tk.Label(infer, text="RED = BOOKED", fg='brown').grid(row=0, column=1, padx=10)
        tk.Label(infer, text="GREEN = AVAILABLE", fg='green').grid(row=0, column=2, padx=10)
        tkinter.ttk.Separator(window, orient=tkinter.HORIZONTAL).grid(row=2, column=0, pady=(0, 5),
                                                                      sticky=tk.EW)
        w = tk.Canvas(window, width=500, height=15)
        w.create_rectangle(10, 0, 490, 10, fill='black')
        w.grid(row=3, column=0)
        tk.Label(window, text="SCREEN").grid(row=4, column=0, pady=(0, 10))
        seats = tk.Frame(window)
        seats.grid(row=5, column=0)
        seatList.clear()
        seatSelected.clear()

        for i in range(4):
            temp = []
            for j in range(15):
                but = tk.Button(seats, bd=2, bg='green', activebackground='forestGreen',
                                command= lambda x=i, y=j: self.selected(x, y))
                temp.append(but)
                but.grid(row=i, column=j, padx=5, pady=5)
            seatList.append(temp)

        tk.Button(window, text="Book Seats", bg='black', fg='white', command=self.book_seats).grid(
            row=6, column=0, pady=10
        )

    def selected(self, i, j):
        if seatList[i][j]['bg'] == 'blue':
            seatList[i][j]['bg'] = 'green'
            seatList[i][j]['activebackground'] = 'forestGreen'
            seatSelected.remove((i, j))
            return

        seatList[i][j]['bg'] = 'blue'
        seatList[i][j]['activebackground'] = 'blue'
        seatSelected.append((i, j))

    @staticmethod
    def book_seats():
        for seat in seatSelected:
            seatList[seat[0]][seat[1]]['bg'] = 'brown'
            seatList[seat[0]][seat[1]]['activebackground'] = 'brown'
            seatList[seat[0]][seat[1]]['relief'] = tk.SUNKEN
            seatList[seat[0]][seat[1]]['state'] = tk.DISABLED


app = Application()
app.mainloop()
