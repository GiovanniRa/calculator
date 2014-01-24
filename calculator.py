"""Simple calculator, realized with Tkinter, Python 2.7.5.
Imports a file containing the class Operation, with functions of the 4 operations and percentage
"""

from Tkinter import *
from operations import *


a = 0
b = 0

op = Operations()


def starting_calculation():
    global a
    a = float(entry1.get())
    entry2.focus_set()


def second_number():
    global b
    b = float(entry2.get())


def adding():
    starting_calculation()
    equal_button.configure(command=add_result)


def add_result():
    second_number()
    output_label.configure(text=op.addiction(a, b))


def subtracting():
    starting_calculation()
    equal_button.configure(command=subtract_result)


def subtract_result():
    second_number()
    output_label.configure(text=op.subtraction(a, b))


def multiplying():
    starting_calculation()
    equal_button.configure(command=multiply_result)


def multiply_result():
    second_number()
    output_label.configure(text=op.multiplication(a, b))


def dividing():
    starting_calculation()
    equal_button.configure(command=divide_result)


def divide_result():
    second_number()
    output_label.configure(text=op.division(a, b))


def percent():
    starting_calculation()
    equal_button.configure(command=percent_result)


def percent_result():
    second_number()
    output_label.configure(text=op.percentage(a, b))


def reset():
    output_label.configure(text=0)
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry1.focus_set()


root = Tk()

root.wm_title("CALCULATOR")

root.wm_minsize(height=150, width=200)


message_label1 = Label(text='num', font=('Verdana', 16))

message_label2 = Label(text='num', font=('Verdana', 16))

output_label = Label(text=0, font=('Verdana', 20))

entry1 = Entry(font=('Verdana', 16), width=10)

entry2 = Entry(font=('Verdana', 16), width=10)

plus_button = Button(text='+', font=('Verdana', 20), command=adding)

minus_button = Button(text='-', font=('Verdana', 20), command=subtracting)

multiply_button = Button(text='*', font=('Verdana', 20), command=multiplying)

divide_button = Button(text='/', font=('Verdana', 20), command=dividing)

reset_button = Button(text='C', font=('Verdana', 16), command=reset)

equal_button = Button(text='=', font=('Verdana', 20))

percent_button = Button(text='%', font=('Verdana', 20), command=percent)


message_label1.grid(row=0, column=0)

message_label2.grid(row=2, column=0)

output_label.grid(row=3, column=1, columnspan=3)

entry1.grid(row=0, column=1, columnspan=5)

entry2.grid(row=2, column=1, columnspan=5)

plus_button.grid(row=1, column=0)

minus_button.grid(row=1, column=1)

multiply_button.grid(row=1, column=2)

divide_button.grid(row=1, column=3)

percent_button.grid(row=1, column=4)

equal_button.grid(row=3, column=4)

reset_button.grid(row=3, column=0)

entry1.focus_set()

mainloop()
