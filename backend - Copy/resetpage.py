import socket
import threading
from tkinter import *
from tkinter import font
from tkinter import ttk 
from tkinter import *
from tkinter import messagebox
import ast
import smtplib
import random

def reset_send_otp():
    loot=Tk()
    loot.title('reset')
    loot.geometry('925x500+300+200')
    loot.configure(bg="#fff")
    loot.resizable(TRUE,TRUE)
    img=PhotoImage(file='login.png')
    Label(loot,image=img,bg='white').place(x=50,y=50)
    frame=Frame(loot,width=350,height=350,bg="white")
    frame.place(x=480,y=70)
    heading=Label(frame,text='Reset Password',fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light',23,'bold'))
    heading.place(x=50,y=5)
    def on_enter(e):
        user.delete(0, 'end')

    def on_leave(e):
            name=user.get()
            if name=='':
                user.insert(0,'Username')

    user= Entry(frame,width=30,fg='black', border=2,bg="white",font=('Microsoft YaHei UI Light', 11))
    user.place(x=60, y=70)
    user.insert(0,'Username')
    user.bind('<FocusIn>', on_enter)
    user.bind('FocusOut', on_leave)
    Button(frame, width=25,pady=6,text='SEND OTP', bg='#57a1f8', fg='white', border=0).place(x=95, y=200)
    loot.mainloop()    
	
		
    
reset_send_otp()   
  

	