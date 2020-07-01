from tkinter import *


root = Tk()


numbers = []

statement = ""

def AddDigit(num):
    global statement
    statement += str(num)

ScreenStatement = Label(root, text=statement).grid(row=0, columnspan=3)

for x in range(9):
    i = x % 3
    j = x // 3
    numbers.append(Button(root, text=str(x + 1)).grid(row=j + 1, column=i, command=AddDigit(x + 1)))

root.mainloop()