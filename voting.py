from tkinter import *
from tkinter import messagebox

count = 0
coun = 0
cou = 0
co = 0
c = 0
List = [2345, 6789, 1100, 3344, 5566]
a = []

def aadh():
    global List,a,fnumber

    fnumber = int(number.get())

    if (fnumber in List) and  (fnumber not in a):
        a.append(fnumber)

        top = Toplevel(main)
        top.geometry("1920x1200")
        def admk():
            global count
            count += 1
            messagebox.showinfo("vote", "Voted for ADMK")
            ret()

        def dmk():
            global coun
            coun += 1
            messagebox.showinfo("vote", "Voted for DMK")
            ret()

        def nt():
            global cou
            cou += 1
            messagebox.showinfo("vote", "Voted for NAAM_THAMIzHAR")
            ret()

        def pmk():
            global co
            co += 1
            messagebox.showinfo("vote", "Voted for PMK")
            ret()

        def bjp():
            global c
            c += 1
            messagebox.showinfo("vote", "Voted for BJP")
            ret()


        label = Label(top, text="VOTING SYSTEM").place(x=150, y=0)
        a1 = Label(top, text="1 ---> AIADMK").place(x=0, y=30)
        a2 = Button(top, command=admk, text="VOTE!").place(x=100, y=30)
        d1 = Label(top, text="2 ---> DMK").place(x=0, y=80)
        d2 = Button(top, command=dmk, text="VOTE!").place(x=100, y=80)
        n1 = Label(top, text="3 ---> NAAM_THAMIZHAR").place(x=0, y=130)
        n2 = Button(top, command=nt, text="VOTE!").place(x=180, y=130)
        p1 = Label(top, text="4 ---> PMK").place(x=0, y=195)
        p2 = Button(top, command=pmk, text="VOTE!").place(x=100, y=195)
        b1 = Label(top, text="5 ---> BJP").place(x=0, y=250)
        b2 = Button(top, command=bjp, text="VOTE!").place(x=100, y=250)



    else:
        messagebox.showwarning("vote", "INCORRECT or Already voted")
        ret()





def votes():
    global entry
    global entryy
    aa=Toplevel(main)
    aa.geometry("1920x1200")

    def ver():
        global entry
        global entryy
        entry = st.get()
        entryy = stt.get()
        if entry == "Voting" and entryy == "vote":
            ab=Toplevel(aa)
            ab.geometry("1920x1200")
            def advote():

                messagebox.showinfo("VOTES IS", count)

            def dmvote():
                messagebox.showinfo("VOTES IS", coun)

            def ntvote():
                messagebox.showinfo("VOTES IS", cou)

            def pmkvote():
                messagebox.showinfo("VOTES IS", co)

            def bjpvote():
                messagebox.showinfo("VOTES", c)

            b3 = Button(ab, command=advote, text="ADMK VOTES").place(x=300, y=0)
            b4 = Button(ab, command=dmvote, text="DMK VOTES").place(x=300, y=50)
            b5 = Button(ab, command=ntvote, text="NAAM THAMIZHAR VOTES").place(x=300, y=100)
            b6 = Button(ab, command=pmkvote, text="PMK VOTES").place(x=300, y=150)
            b7 = Button(ab, command=bjpvote, text="bjp VOTES").place(x=300, y=200)
        else:
            messagebox.showwarning("Warning","Invalid")
    lb=Label(aa,text="Please enter The Below Credentials",font=("Times New Roman",20)).place(x=455,y=100)
    l = Label(aa, text="Username").place(x=455, y=170)
    E = Entry(aa, width=30, textvariable=st).place(x=455, y=200)
    l = Label(aa, text="password").place(x=455,y=240)
    EE = Entry(aa, width=30, textvariable=stt).place(x=455, y=260)
    bb = Button(aa, command=ver, text="submit").place(x=455,y=300)


def ret():
    aad = Toplevel(main)
    aad.geometry("1920x1200")
    aad.configure(background="light slate gray")
    global number
    number = StringVar()
    r = Label(aad, text=" VOTING SYSTEM", font=("Arial Bold", 20)).place(x=100, y=0)
    ra = Label(aad, text="Enter Your AADHAR number").place(x=150, y=70)
    e = Entry(aad, width=30, textvariable=number).place(x=150, y=55)
    bn = Button(aad, command=aadh, text="Submit").place(x=150, y=100)


main = Tk()
main.geometry("1920x1200")
frame = Frame(main)
frame.pack()
main.configure(background="light slate gray")
st = StringVar()
stt = StringVar()
btt = Button(main, command=ret, text="VOTE!!", width=30 , pady = 10).place(x=500, y=400)
bnn = Button(main,command = votes,text =" See the Votes" , width =30 , pady =10).place(x=500, y =300 )
main.mainloop()

