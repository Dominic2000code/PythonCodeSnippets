from tkinter import *

root = Tk()
root.title("Sid's Calculator")
root.iconbitmap(r"C:\Users\Dominic\Pictures\New folder\Calculator_30001.ico")
screen = Entry(root, width=50, borderwidth=5)
screen.grid(row=0, column=0, columnspan=6, padx=10, pady=10)


def addition():
    previousNum = screen.get()
    global prevNum
    global operator
    prevNum = int(previousNum)
    operator = "addition"
    screen.delete(0, END)


def multiplication():
    previousNum = screen.get()
    global prevNum
    global operator
    prevNum = int(previousNum)
    operator = "multiplication"
    screen.delete(0, END)


def subtraction():
    previousNum = screen.get()
    global prevNum
    global operator
    prevNum = int(previousNum)
    operator = "subtraction"
    screen.delete(0, END)


def division():
    previousNum = screen.get()
    global prevNum
    global operator
    prevNum = int(previousNum)
    operator = "division"
    screen.delete(0, END)


def equal():
    secondNum = int(screen.get())
    screen.delete(0, END)
    if operator == "addition":
        screen.insert(0, prevNum + secondNum)

    elif operator == "subtraction":
        screen.insert(0, prevNum - secondNum)

    elif operator == "multiplication":
        screen.insert(0, prevNum * secondNum)

    elif operator == "division":
        screen.insert(0, prevNum / secondNum)


def square():
    previousNum = int(screen.get())
    screen.delete(0, END)
    screen.insert(0, previousNum * previousNum)


def percentage():
    previousNum = float(screen.get())
    screen.delete(0, END)
    screen.insert(0, previousNum / 100)


def sqrt():
    previousNum = float(screen.get())
    screen.delete(0, END)
    screen.insert(0, previousNum ** 0.5)


def clear():
    screen.delete(0, END)


def buttonOnclick(number):
    current = screen.get()
    screen.delete(0, END)
    screen.insert(END, str(current) + str(number))


# the code below creates a button
button_1 = Button(root, text="1", padx=40, pady=20, bg="black", fg="white", command=lambda: buttonOnclick(1))
button_2 = Button(root, text="2", padx=40, pady=20, bg="black", fg="white", command=lambda: buttonOnclick(2))
button_3 = Button(root, text="3", padx=40, pady=20, bg="black", fg="white", command=lambda: buttonOnclick(3))
button_4 = Button(root, text="4", padx=40, pady=20, bg="black", fg="white", command=lambda: buttonOnclick(4))

button_5 = Button(root, text="5", padx=40, pady=20, bg="black", fg="white", command=lambda: buttonOnclick(5))
button_6 = Button(root, text="6", padx=40, pady=20, bg="black", fg="white", command=lambda: buttonOnclick(6))
button_7 = Button(root, text="7", padx=40, pady=20, bg="black", fg="white", command=lambda: buttonOnclick(7))
button_8 = Button(root, text="8", padx=40, pady=20, bg="black", fg="white", command=lambda: buttonOnclick(8))

button_9 = Button(root, text="9", padx=40, pady=20, bg="black", fg="white", command=lambda: buttonOnclick(9))
button_0 = Button(root, text="0", padx=40, pady=20, bg="black", fg="white", command=lambda: buttonOnclick(0))
button_division = Button(root, text="/", padx=40, pady=20, bg="black", fg="white", command=division)
button_multiplication = Button(root, text="*", padx=40, pady=20, bg="grey", fg="white", command=multiplication)

button_subtraction = Button(root, text="-", padx=40, pady=20, bg="grey", fg="white", command=subtraction)
button_addition = Button(root, text="+", padx=40, pady=20, bg="grey", fg="white", command=addition)
button_square = Button(root, text="^2", padx=35, pady=20, bg="black", fg="white", command=square)
button_equal = Button(root, text="=", padx=40, pady=20, bg="grey", fg="white", command=equal)

button_sqrt = Button(root, text="sqrt", padx=32, pady=20, bg="black", fg="white", command=sqrt)
button_percentage = Button(root, text="%", padx=40, pady=20, bg="black", fg="white", command=percentage)
button_clear = Button(root, text="C", padx=38, pady=20, bg="grey", fg="white", command=clear)

# the code below sets up the button for viewing

button_square.grid(column=0, row=5)
button_0.grid(column=1, row=5)
button_division.grid(column=2, row=5)
button_equal.grid(column=3, row=5)

button_1.grid(column=0, row=4)
button_2.grid(column=1, row=4)
button_3.grid(column=2, row=4)
button_addition.grid(column=3, row=4)

button_4.grid(column=0, row=3)
button_5.grid(column=1, row=3)
button_6.grid(column=2, row=3)
button_subtraction.grid(column=3, row=3)

button_7.grid(column=0, row=2)
button_8.grid(column=1, row=2)
button_9.grid(column=2, row=2)
button_multiplication.grid(column=3, row=2)

button_sqrt.grid(row=1, column=0)
button_percentage.grid(row=1, column=1)
button_clear.grid(row=1, column=2)

root.mainloop()
