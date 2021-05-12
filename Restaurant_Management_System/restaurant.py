from tkinter import *
import random
import time

root = Tk()
root.geometry("1280x700+0+0")
root.title("Restaurant Management System")

Tops = Frame(root, bg="black", width=1280, height=500, relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, width=900, height=700, relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root, width=400, height=700, relief=SUNKEN)
f2.pack(side=RIGHT)

localtime = time.asctime(time.localtime(time.time()))
lbl_info = Label(Tops, font=('arial', 30, 'bold'), text="Restaurant Management System",
                 fg="blue", bd=10, anchor=W)
lbl_info.grid(row=0, column=0)

lbl_info = Label(Tops, font=('arial', 30, 'bold'), text=localtime, fg="red", anchor=W)
lbl_info.grid(row=1, column=0)

text_input = StringVar()
operator = ""

text_display = Entry(f2, font=('arial', 20, 'bold'), textvariable=text_input, bd=5,
                     insertwidth=7, bg='green', justify=RIGHT)

text_display.grid(columnspan=4)


def btnclick(numbers):
    global operator
    operator = operator + str(numbers)
    text_input.set(operator)


def clrdisplay():
    global operator
    operator = ""
    text_input.set("")


def equals():
    global operator
    sum_up = str(eval(operator))
    text_input.set(sum_up)
    operator = ""


def ref():
    x = random.randint(12000, 50000)
    random_ref = str(x)
    rand.set(random_ref)

    fries = float(Fries.get())
    lunch_meal = float(Large_Fries.get())
    burger_meal = float(Burger.get())
    pizza_meal = float(Fillet.get())
    cheese_burger = float(Cheese_Burger.get())
    drinks = float(Drinks.get())

    fries_cost = fries * 25
    lunch_cost = lunch_meal * 40
    burger_cost = burger_meal * 35
    pizza_cost = pizza_meal * 50
    cheese_burger_cost = cheese_burger * 30
    drinks_cost = drinks * 35

    meal_cost = "Rs. ", str('%.2f' % (fries_cost + lunch_cost + burger_cost +
                                      pizza_cost + cheese_burger_cost + drinks_cost))
    tax_payable = ((fries_cost + lunch_cost + burger_cost +
                    pizza_cost + cheese_burger_cost + drinks_cost) * 0.33)
    ser_charge = ((fries_cost + lunch_cost + burger_cost +
                   pizza_cost + cheese_burger_cost + drinks_cost) * 0.01)
    service = "Rs. ", str('%.2f' % ser_charge)

    total_cost = fries_cost + lunch_cost + burger_cost + pizza_cost + cheese_burger_cost + drinks_cost

    overall_cost = "Rs. ", str(tax_payable + total_cost + ser_charge)

    paid_tax = "Rs. ", str('%.2f' % tax_payable)

    Service_Charge.set(service)
    Cost.set(meal_cost)
    Tax.set(paid_tax)
    SubTotal.set(meal_cost)
    Total.set(overall_cost)


def g_exit():
    root.destroy()


def reset():
    rand.set("")
    Fries.set("")
    Large_Fries.set("")
    Burger.set("")
    Fillet.set("")
    Cheese_Burger.set("")
    Drinks.set("")
    Total.set("")
    SubTotal.set("")
    Cost.set("")
    Tax.set("")
    Service_Charge.set("")


btn7 = Button(f2, padx=16, pady=16, bd=4, fg="white", font=('arial', 20, 'bold'),
              text="7", bg="black", command=lambda: btnclick(7))
btn7.grid(row=2, column=0)

btn8 = Button(f2, padx=16, pady=16, bd=4, fg="white", font=('arial', 20, 'bold'),
              text="8", bg="black", command=lambda: btnclick(8))
btn8.grid(row=2, column=1)

btn9 = Button(f2, padx=16, pady=16, bd=4, fg="white", font=('arial', 20, 'bold'),
              text="9", bg="black", command=lambda: btnclick(9))
btn9.grid(row=2, column=2)

addition = Button(f2, padx=16, pady=16, bd=4, fg="white", font=('arial', 20, 'bold'),
                  text="+", bg="black", command=lambda: btnclick("+"))
addition.grid(row=2, column=3)

btn4 = Button(f2, padx=16, pady=16, bd=4, fg="white", font=('arial', 20, 'bold'),
              text="4", bg="black", command=lambda: btnclick(4))
btn4.grid(row=3, column=0)

btn5 = Button(f2, padx=16, pady=16, bd=4, fg="white", font=('arial', 20, 'bold'),
              text="5", bg="black", command=lambda: btnclick(5))
btn5.grid(row=3, column=1)

btn6 = Button(f2, padx=16, pady=16, bd=4, fg="white", font=('arial', 20, 'bold'),
              text="4", bg="black", command=lambda: btnclick(5))
btn6.grid(row=3, column=2)

subtraction = Button(f2, padx=16, pady=16, bd=4, fg="white", font=('arial', 20, 'bold'),
                     text="-", bg="black", command=lambda: btnclick("-"))
subtraction.grid(row=3, column=3)

btn1 = Button(f2, padx=16, pady=16, bd=4, fg="white", font=('arial', 20, 'bold'),
              text="1", bg="black", command=lambda: btnclick(1))
btn1.grid(row=4, column=0)

btn2 = Button(f2, padx=16, pady=16, bd=4, fg="white", font=('arial', 20, 'bold'),
              text="2", bg="black", command=lambda: btnclick(2))
btn2.grid(row=4, column=1)

btn3 = Button(f2, padx=16, pady=16, bd=4, fg="white", font=('arial', 20, 'bold'),
              text="3", bg="black", command=lambda: btnclick(3))
btn3.grid(row=4, column=2)

multiply = Button(f2, padx=16, pady=16, bd=4, fg="white", font=('arial', 20, 'bold'),
                  text="*", bg="black", command=lambda: btnclick("*"))
multiply.grid(row=4, column=3)

btn0 = Button(f2, padx=16, pady=16, bd=4, fg="white", font=('arial', 20, 'bold'),
              text="0", bg="black", command=lambda: btnclick(0))
btn0.grid(row=5, column=0)

btnc = Button(f2, padx=16, pady=16, bd=4, fg="white", font=('arial', 20, 'bold'),
              text="c", bg="black", command=clrdisplay)
btnc.grid(row=5, column=1)

decimal = Button(f2, padx=16, pady=16, bd=4, fg="white", font=('arial', 20, 'bold'),
                 text=".", bg="black", command=lambda: btnclick("."))
decimal.grid(row=5, column=2)

division = Button(f2, padx=16, pady=16, bd=4, fg="white", font=('arial', 20, 'bold'),
                  text="/", bg="black", command=lambda: btnclick("/"))
division.grid(row=5, column=3)

btn_equal = Button(f2, padx=16, pady=16, bd=4, fg="white", font=('arial', 20, 'bold'),
                   text="=", bg="black", command=equals)
btn_equal.grid(columnspan=4)

rand = StringVar()
Fries = StringVar()
Large_Fries = StringVar()
Burger = StringVar()
Fillet = StringVar()
SubTotal = StringVar()
Total = StringVar()
Service_Charge = StringVar()
Drinks = StringVar()
Tax = StringVar()
Cost = StringVar()
Cheese_Burger = StringVar()

lbl_reference = Label(f1, font=('arial', 16, 'bold'), text="Order No.", fg="black",
                      bd=10, anchor=W)
lbl_reference.grid(row=0, column=0)
txt_reference = Entry(f1, font=('arial', 17, 'bold'), textvariable=rand, bd=6,
                      insertwidth=4, bg="red", justify=RIGHT)
txt_reference.grid(row=0, column=1)

lbl_fries = Label(f1, font=('arial', 16, 'bold'), text="Fries Meal", fg="black",
                  bd=10, anchor=W)
lbl_fries.grid(row=1, column=0)
txt_fries = Entry(f1, font=('arial', 17, 'bold'), textvariable=Fries, bd=6,
                  insertwidth=4, bg="red", justify=RIGHT)
txt_fries.grid(row=1, column=1)

lbl_large_fries = Label(f1, font=('arial', 16, 'bold'), text="Large Fries Meal", fg="black",
                        bd=10, anchor=W)
lbl_large_fries.grid(row=2, column=0)
txt_large_fries = Entry(f1, font=('arial', 17, 'bold'), textvariable=Large_Fries, bd=6,
                        insertwidth=4, bg="red", justify=RIGHT)
txt_large_fries.grid(row=2, column=1)

lbl_large_fries = Label(f1, font=('arial', 16, 'bold'), text="Large Fries Meal", fg="black",
                        bd=10, anchor=W)
lbl_large_fries.grid(row=2, column=0)
txt_large_fries = Entry(f1, font=('arial', 17, 'bold'), textvariable=Large_Fries, bd=6,
                        insertwidth=4, bg="red", justify=RIGHT)
txt_large_fries.grid(row=2, column=1)

lbl_burger = Label(f1, font=('arial', 16, 'bold'), text="Burger", fg="black",
                   bd=10, anchor=W)
lbl_burger.grid(row=3, column=0)
txt_burger = Entry(f1, font=('arial', 17, 'bold'), textvariable=Burger, bd=6,
                   insertwidth=4, bg="red", justify=RIGHT)
txt_burger.grid(row=3, column=1)

lbl_fillet = Label(f1, font=('arial', 16, 'bold'), text="Fillet", fg="black",
                   bd=10, anchor=W)
lbl_fillet.grid(row=4, column=0)
txt_fillet = Entry(f1, font=('arial', 17, 'bold'), textvariable=Fillet, bd=6,
                   insertwidth=4, bg="red", justify=RIGHT)
txt_fillet.grid(row=4, column=1)

lbl_cheese_burger = Label(f1, font=('arial', 16, 'bold'), text="Cheese Burger", fg="black",
                          bd=10, anchor=W)
lbl_cheese_burger.grid(row=5, column=0)
txt_cheese_burger = Entry(f1, font=('arial', 17, 'bold'), textvariable=Cheese_Burger, bd=6,
                          insertwidth=4, bg="red", justify=RIGHT)
txt_cheese_burger.grid(row=5, column=1)

lbl_drinks = Label(f1, font=('arial', 16, 'bold'), text="Drinks", fg="black",
                   bd=10, anchor=W)
lbl_drinks.grid(row=0, column=2)
txt_drinks = Entry(f1, font=('arial', 17, 'bold'), textvariable=Drinks, bd=6,
                   insertwidth=4, bg="red", justify=RIGHT)
txt_drinks.grid(row=0, column=3)

lbl_cost = Label(f1, font=('arial', 16, 'bold'), text="Cost", fg="black",
                 bd=10, anchor=W)
lbl_cost.grid(row=1, column=2)
txt_cost = Entry(f1, font=('arial', 17, 'bold'), textvariable=Cost, bd=6,
                 insertwidth=4, bg="red", justify=RIGHT)
txt_cost.grid(row=1, column=3)

lbl_service_charge = Label(f1, font=('arial', 16, 'bold'), text="Service Charge", fg="black",
                           bd=10, anchor=W)
lbl_service_charge.grid(row=2, column=2)
txt_service_charge = Entry(f1, font=('arial', 17, 'bold'), textvariable=Service_Charge, bd=6,
                           insertwidth=4, bg="red", justify=RIGHT)
txt_service_charge.grid(row=2, column=3)

lbl_tax = Label(f1, font=('arial', 16, 'bold'), text="Tax", fg="black",
                bd=10, anchor=W)
lbl_tax.grid(row=3, column=2)
txt_tax = Entry(f1, font=('arial', 17, 'bold'), textvariable=Tax, bd=6,
                insertwidth=4, bg="red", justify=RIGHT)
txt_tax.grid(row=3, column=3)

lbl_sub_total = Label(f1, font=('arial', 16, 'bold'), text="Sub Total", fg="black",
                      bd=10, anchor=W)
lbl_sub_total.grid(row=4, column=2)
txt_sub_total = Entry(f1, font=('arial', 17, 'bold'), textvariable=SubTotal, bd=6,
                      insertwidth=4, bg="red", justify=RIGHT)
txt_sub_total.grid(row=4, column=3)

lbl_total = Label(f1, font=('arial', 16, 'bold'), text="Total", fg="black",
                  bd=10, anchor=W)
lbl_total.grid(row=5, column=2)
txt_total = Entry(f1, font=('arial', 17, 'bold'), textvariable=Total, bd=6,
                  insertwidth=4, bg="red", justify=RIGHT)
txt_total.grid(row=5, column=3)

btn_total = Button(f1, padx=16, pady=8, fg="white", font=('arial', 16, 'bold'),
                   width=10, text="TOTAL", bg="black", command=ref)
btn_total.grid(row=7, column=1)

btn_reset = Button(f1, padx=16, pady=8, fg="white", font=('arial', 16, 'bold'),
                   width=10, text="RESET", bg="black", command=reset)
btn_reset.grid(row=7, column=2)

btn_exit = Button(f1, padx=16, pady=8, fg="white", font=('arial', 16, 'bold'),
                  width=10, text="EXIT", bg="black", command=g_exit)
btn_exit.grid(row=7, column=3)


def price():
    price_root = Tk()
    price_root.geometry("600x220")
    price_root.title("Price List")
    x = Frame(price_root, bg="white", width=600, height=220, relief=SUNKEN)
    x.pack(side=TOP)
    price_lbl_info = Label(x, font=('arial', 15, 'bold'), text="ITEM", fg="red", bd=5)
    price_lbl_info.grid(row=0, column=0)
    price_lbl_info = Label(x, font=('arial', 15, 'bold'), text="____________", fg="black", bd=5, anchor=W)
    price_lbl_info.grid(row=0, column=2)
    price_lbl_info = Label(x, font=('arial', 15, 'bold'), text="PRICE", fg="red", bd=5, anchor=W)
    price_lbl_info.grid(row=0, column=5)

    price_lbl_info = Label(x, font=('arial', 15, 'bold'), text="Fries Meal", fg="steel blue", bd=5)
    price_lbl_info.grid(row=1, column=0)
    price_lbl_info = Label(x, font=('arial', 15, 'bold'), text="25", fg="steel blue", bd=5)
    price_lbl_info.grid(row=1, column=5)

    price_lbl_info = Label(x, font=('arial', 15, 'bold'), text="Lunch Meal", fg="steel blue", bd=5)
    price_lbl_info.grid(row=2, column=0)
    price_lbl_info = Label(x, font=('arial', 15, 'bold'), text="40", fg="steel blue", bd=5)
    price_lbl_info.grid(row=2, column=5)

    price_lbl_info = Label(x, font=('arial', 15, 'bold'), text="Burger Meal", fg="steel blue", bd=5)
    price_lbl_info.grid(row=3, column=0)
    price_lbl_info = Label(x, font=('arial', 15, 'bold'), text="35", fg="steel blue", bd=5)
    price_lbl_info.grid(row=3, column=5)

    price_lbl_info = Label(x, font=('arial', 15, 'bold'), text="Pizza Meal", fg="steel blue", bd=5)
    price_lbl_info.grid(row=4, column=0)
    price_lbl_info = Label(x, font=('arial', 15, 'bold'), text="50", fg="steel blue", bd=5)
    price_lbl_info.grid(row=4, column=5)

    price_lbl_info = Label(x, font=('arial', 15, 'bold'), text="Cheese Burger", fg="steel blue", bd=5)
    price_lbl_info.grid(row=5, column=0)
    price_lbl_info = Label(x, font=('arial', 15, 'bold'), text="30", fg="steel blue", bd=5)
    price_lbl_info.grid(row=5, column=5)

    price_lbl_info = Label(x, font=('arial', 15, 'bold'), text="Drinks", fg="steel blue", bd=5)
    price_lbl_info.grid(row=6, column=0)
    price_lbl_info = Label(x, font=('arial', 15, 'bold'), text="35", fg="steel blue", bd=5)
    price_lbl_info.grid(row=6, column=5)


btn_price = Button(f1, padx=16, pady=8, fg="white", font=('arial', 16, 'bold'),
                   width=10, text="PRICE", bg="black", command=price)
btn_price.grid(row=7, column=0)

root.mainloop()
