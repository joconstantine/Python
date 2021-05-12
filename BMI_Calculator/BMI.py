from tkinter import *

root = Tk()
root.title("BMI Calculator")
root.configure(width=100, height=100)
root.configure(bg="black")


def calc():
    computed_bmi = BMI_Val(mass.get(), height.get())
    bmi_val.set(format(computed_bmi, ".2f"))
    computed_status = getStatus()
    status.set(computed_status)


def BMI_Val(m, h):
    return m / (h ** 2)


def getHeight():
    return height


def getWidth():
    return mass


def clear():
    status.set("")
    bmi_val.set("")
    mass_entry.delete(0, END)
    height_entry.delete(0, END)


def getStatus():
    if bmi_val.get() > 40:
        return "You are obese class 3"
    elif bmi_val.get() > 35:
        return "You are obese class 2"
    elif bmi_val.get() > 30:
        return "You are obese class 1"
    elif bmi_val.get() > 25:
        return "You are overweight"
    elif bmi_val.get() > 18.5:
        return "You are normal"
    elif bmi_val.get() > 17:
        return "You are mild thin"
    else:
        return "You are moderately thin"


height = DoubleVar()
h_label = Label(root, text="Height", fg="red", bg="black", font=("Calibri 14 bold"),
                pady=5, padx=8)
height_entry = Entry(root, textvariable=height)
h_label.grid(row=2)
height_entry.grid(row=2, column=1, columnspan=2, padx=5)

mass = DoubleVar()
w_label = Label(root, text="Mass", fg="red", bg="black", font=("Calibri 14 bold"),
                pady=10, padx=2)
mass_entry = Entry(root, textvariable=mass)
w_label.grid(row=3)
mass_entry.grid(row=3, column=1, columnspan=2, padx=5)

bmi_val = DoubleVar()
status = StringVar()

bmi_label = Label(root, text="BMI: ", fg="blue", bg="black", font=("Calibri 14 bold"),
                  padx=2, pady=10, justify=LEFT)
status_label = Label(root, text="Status: ", fg="blue", bg="black", font=("Calibri 14 bold"),
                     padx=2, pady=10)
status_msg = Label(root, textvariable=status, fg="white", bg="black", font=("Calibri 14 bold"),
                   padx=2, pady=10)
bmi_val_label = Label(root, textvariable=bmi_val, fg="white", bg="black", font=("Calibri 14 bold"),
                      padx=2, pady=10)
bmi_label.grid(row=6)
bmi_val_label.grid(row=6, column=1)
status_label.grid(row=7)
status_msg.grid(row=7, column=1)

calculate_button = Button(root, text="Calculate", command=calc, fg="black", bg="white", font=("Calibri 14 bold"))
clear_button = Button(root, text="Reset", command=clear, fg="black", bg="white", font=("Calibri 14 bold"))
calculate_button.grid(row=8)
clear_button.grid(row=8, column=3)

root.mainloop()
