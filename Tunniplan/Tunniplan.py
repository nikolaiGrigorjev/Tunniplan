from tkinter import *
from tkinter import ttk


okno=Tk()
okno.geometry("1600x900")
okno.title("Tunniplan TARpv20")

def help():
    if a==0:
        tabs.select(0)
    elif a==1:
        tabs.select(1)
    elif a==2:
        tabs.select(2)


lbl=Label(okno,text="Tunniplaan 01.02.2021 - 07.02.2021",font="Calibri 15",fg="purple",bg="white",borderwidth="4",relief="groove")
lbl.grid(row=0,column=0,columnspan=11)




M=Menu(okno)
m1=Menu(M,tearoff=1)
okno.config(menu=M)
M.add_cascade(label="TIMETABLE",menu=m1)
m1.add_command(label="25.01.2021-31.01.2021",command=help)

lbl00=Label(okno,text="                       ",font="Calibri 10",fg="black",bg="white",borderwidth="4",relief="groove")
lbl00.grid(row=2,column=0)
lbl0=Label(okno,text="0(7:40-8:25)",font="Calibri 10",fg="black",bg="white",borderwidth="4",relief="groove")
lbl0.grid(row=2,column=1)
lbl1=Label(okno,text="1(8:30-9:15)",font="Calibri 10",fg="black",bg="white",borderwidth="4",relief="groove")
lbl1.grid(row=2,column=2)
lbl2=Label(okno,text="2(9:20-10:05)",font="Calibri 10",fg="black",bg="white",borderwidth="4",relief="groove")
lbl2.grid(row=2,column=3)
lbl3=Label(okno,text="3(10:10-10:55)",font="Calibri 10",fg="black",bg="white",borderwidth="4",relief="groove")
lbl3.grid(row=2,column=4)
lbl4=Label(okno,text="4(11:00-11:45)",font="Calibri 10",fg="black",bg="white",borderwidth="4",relief="groove")
lbl4.grid(row=2,column=5)
lbl5=Label(okno,text="5(11:50-12:35)",font="Calibri 10",fg="black",bg="white",borderwidth="4",relief="groove")
lbl5.grid(row=2,column=6)
lbl6=Label(okno,text="6(12:40-13:25)",font="Calibri 10",fg="black",bg="white",borderwidth="4",relief="groove")
lbl6.grid(row=2,column=7)
lbl7=Label(okno,text="7(13:30-14:15)",font="Calibri 10",fg="black",bg="white",borderwidth="4",relief="groove")
lbl7.grid(row=2,column=8)
lbl8=Label(okno,text="8(14:20-15:05)",font="Calibri 10",fg="black",bg="white",borderwidth="4",relief="groove")
lbl8.grid(row=2,column=9)
lbl9=Label(okno,text="9(15:10-15:55)",font="Calibri 10",fg="black",bg="white",borderwidth="4",relief="groove")
lbl9.grid(row=2,column=10)
lbl10=Label(okno,text="10(16:00-16:45)",font="Calibri 10",fg="black",bg="white",borderwidth="4",relief="groove")
lbl10.grid(row=2,column=11)
lbl11=Label(okno,text="11(16:50-17:35)",font="Calibri 10",fg="black",bg="white",borderwidth="4",relief="groove")
lbl11.grid(row=2,column=12)

lblpä=Label(okno,text=" Esmaspäev ",font="Calibri 10",fg="black",bg="white",borderwidth="4",relief="groove",height=5)
lblpä.grid(row=4,column=0,rowspan=3)
lblpä=Label(okno,text="   Teisepäev ",font="Calibri 10",fg="black",bg="white",borderwidth="4",relief="groove",height=5)
lblpä.grid(row=7,column=0)
lblpä=Label(okno,text=" Kolmapäev ",font="Calibri 10",fg="black",bg="white",borderwidth="4",relief="groove",height=5)
lblpä.grid(row=10,column=0)
lblpä=Label(okno,text="   Neljapäev ",font="Calibri 10",fg="black",bg="white",borderwidth="4",relief="groove",height=5)
lblpä.grid(row=13,column=0)
lblpä=Label(okno,text="      Reede     ",font="Calibri 10",fg="black",bg="white",borderwidth="4",relief="groove",height=5)
lblpä.grid(row=16,column=0)


lblurok=Label(okno,text="Geo(ee-k,Mari Speek,B239)",font="Calibri 5",fg="black",bg="white",borderwidth="4",relief="groove",height=3)
lblurok.grid(row=3,column=2)



okno.mainloop()