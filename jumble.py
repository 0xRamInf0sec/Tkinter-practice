import tkinter
from tkinter import *
import random
from tkinter import messagebox

answers = ["python","java","swift","canada","india","america","london"]

words = ["nptoyh","avja","wfsit","cdanaa","aidin","aiearcm","odnlon"]
num =  random.randrange(0, len(words))

def show():
    for i in num:
        if i == "nptoyh":
            messagebox.showwarning("Hint","Language")
            break;
        elif i == "avja":
            messagebox.showwarning("Hint", "Useful Language")
            break;
        elif i == "wfsit":
            messagebox.showwarning("Hint", "car")
            break;
        elif i == "cdanaa":
            messagebox.showwarning("Hint", "place")
            break;
        elif i == "aidin":
            messagebox.showwarning("Hint", "emblem")
            break;
        elif i == "aiearcm":
            messagebox.showwarning("Hint", "no 1")
            break;
        else:
            messagebox.showwarning("Hint", "joy")
            break;

def default():
    global words,answers,num
    lbl.config(text = words[num])

def res():
    global words,answers,num
    num = random.randrange(0, len(words))
    lbl.config(text = words[num])
    e1.delete(0, END)


def checkans():
    global words,answers,num
    var = e1.get()
    if var == answers[num]:
        messagebox.showinfo("Success", "This is a correct answer")
        res()
    else:
        messagebox.showerror("Error", "This is not Correct")
        e1.delete(0, END)




root = tkinter.Tk()
root.geometry("350x400+400+300")
root.title("Jumbbled")
root.configure(background = "#667E93")

lbl = Label(root,text = "",font = ("Verdana", 18))
lbl.pack(pady = 30,ipady=10,ipadx=10)
ans1 = StringVar()
e1 = Entry( root,font = ("Verdana", 16),textvariable = ans1)
e1.pack(ipady=5,ipadx=5)

btncheck = Button(root, text = "Check",font = ("Comic sans ms", 16),width = 16,bg = "#4c4b4b",fg = "#6ab04c",command = checkans)
btncheck.pack(pady = 40)

btnreset = Button(root,text = "Reset",font = ("Comic sans ms", 16),width = 16,bg = "#4c4b4b",fg = "#EA425C",command = res)
btnreset.pack()
btnhint=Button(root,text="Hint",font=("Comic sans ms",16),width=10,command=show).place(x=0,y=250)
default()
root.mainloop()
