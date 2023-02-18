from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox

GUI=Tk()#หน้าจอหลัก
GUI.title('โปรแกรมบันทึกข้อมูล')#ชื่อโปรแกรม
GUI.geometry('500x500')#ขนาดหน้าจอ

L1=Label(GUI,text='สีประจำวัน',font=('Angsana New',30),fg='green')
L1.place(x=190,y=20)

#############
def Button1():
    text='สีแดง'
    messagebox.showinfo('สีประจำวัน',text)
def Button2():
    text='สีเหลือง'
    messagebox.showinfo('สีประจำวัน',text)
def Button3():
    text='สีชมพู'
    messagebox.showinfo('สีประจำวัน',text)
def Button4():
    text='สีเขียว'
    messagebox.showinfo('สีประจำวัน',text)
def Button5():
    text='สีส้ม'
    messagebox.showinfo('สีประจำวัน',text)
def Button6():
    text='สีฟ้า'
    messagebox.showinfo('สีประจำวัน',text)
def Button7():
    text='สีม่วง'
    messagebox.showinfo('สีประจำวัน',text)
#############

FB1=Frame(GUI)
FB1.place(x=50,y=100)
B1=ttk.Button(FB1,text='วันอาทิตย์',command=Button1)
B1.pack(ipadx=20,ipady=20)
############
FB2=Frame(GUI)
FB2.place(x=200,y=100)
B2=ttk.Button(FB2,text='วันจันทร์',command=Button2)
B2.pack(ipadx=20,ipady=20)
#############
FB3=Frame(GUI)
FB3.place(x=350,y=100)
B3=ttk.Button(FB3,text='วันอังคาร',command=Button3)
B3.pack(ipadx=20,ipady=20)
#############
FB4=Frame(GUI)
FB4.place(x=50,y=200)
B4=ttk.Button(FB4,text='วันพุธ',command=Button4)
B4.pack(ipadx=20,ipady=20)
#############
FB5=Frame(GUI)
FB5.place(x=200,y=200)
B5=ttk.Button(FB5,text='วันพฤหัสบดี',command=Button5)
B5.pack(ipadx=20,ipady=20)
#############
FB6=Frame(GUI)
FB6.place(x=350,y=200)
B6=ttk.Button(FB6,text='วันศุกร์',command=Button6)
B6.pack(ipadx=20,ipady=20)
#############
FB7=Frame(GUI)
FB7.place(x=200,y=300)
B7=ttk.Button(FB7,text='วันเสาร์',command=Button7)
B7.pack(ipadx=20,ipady=20)
#############



GUI.mainloop()
