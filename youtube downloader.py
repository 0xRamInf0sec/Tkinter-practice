import webbrowser
from tkinter import *



main = Tk()
main.geometry("1920x1200")
main.configure(background="light slate gray")
link = StringVar()
flink = link.get()
def ur():
    global flink
    flink=flink[:12]+"ss"+flink[12:]
    webbrowser.open(flink)
label=Label(main,text="Enter the Link").place(x=500,y=200)
entry=Entry(main, width=30, textvariable=link).place(x=150, y=55)
btt = Button(main, command=ur, text="Download", width=30 , pady = 10).place(x=500, y=400)