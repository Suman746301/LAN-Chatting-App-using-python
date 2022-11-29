from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import ast
import smtplib
import random
import socket
import os


root=Tk()

root.title("Shareit")
root.geometry("450x560+500+200")

root.configure(bg="#f4fdfe")
root.resizable(False,False)





def Send():
    window=Toplevel(root)
    window.title("send")
    window.geometry("450x560+500+200")
    window.configure(bg="#f4fdfe")
    window.resizable(False,False)
    
    def select_file():
        global filename
        filename=filedialog.askopenfilename(initialdir=os.getcwd(),title="Select Image File",
                                            filetypes=(("file_type","*.txt"),("all files","*.*")))
        
    def sender():
        s=socket.socket()
        host=socket.gethostname()
        port=8080
        s.bind((host,port))
        
        s.listen(1)
        print(host)
        print("waiting for any incoming connection ,..........")
        conn,addr=s.accept()
        file=open(filename,"rb")    
        file_data=file.read(1024)
        conn.send(file_data)
        print("data has been transmitted success full")
        

    
    #icon
    
    image_icon1=PhotoImage(file="images/send.png")
    window.iconphoto(False,image_icon1)
    
    Sbackground=PhotoImage(file="images/send.png")
    Label(window,image=Sbackground).place(x=-2,y=0)
    Mbackground=PhotoImage(file="images/send.png")
    Label(window,image=Mbackground,bg="#f4fdfe").place(x=100,y=260)
    
    host=socket.gethostname()
    Label(window,text=f'ID: {host}',bg="white",fg="black").place(x=140,y=290)
    
    Button(window,text="+select file",width=10,height=1,font=("arial",14,"bold"),bg="#fff",fg="#000",command=select_file).place(x=160,y=150 )
    Button(window,text="SEND",width=8,height=1,font=("arial",14,"bold"),bg="#fff",fg="#000",command=sender).place(x=300,y=150 )
    window.mainloop()
    
    
    
def Receive():
<<<<<<< HEAD
=======
    
>>>>>>> 9d9a4b72a1a38960b4bf486eb0573e2af35a7c38
    main=Toplevel(root)
    main.title("receive")
    main.geometry("450x560+500+200")
    main.configure(bg="#f4fdfe")
    main.resizable(False,False)
    main.mainloop()
    
    
    def receiver():
        ID =SenderID.get()
        filename1=incoming_file.get()
        
        s=socket.socket()
       
        port=8080
        s.connect((ID,port))
        file=open(filename1,"wb")
        file_data=s.recv(1024)
        file.write(file_data)
        file.close()
        print("file hads been received")
        
      
        
     
        
        
    
    #icon
    
    image_icon1=PhotoImage(file="images/receive.png")
    main.iconphoto(False,image_icon1)




    
    Hbackground=PhotoImage(file="images/send.png")
    Label(main,image=Hbackground).place(x=-2,y=0)
    
    logo=PhotoImage(file="images/send.png")##########profile pnng
    Label(main,image=logo,bg="#f4fdfe").place(x=10,y=250)
    
    Label(main,text="receive",font=("arial",20),bg="#f4fdfe").place(x=100,y=280)
    
    Label(main,text="input sende id ",font=("arial",10,"bold"),bg="#f4fdfe").place(x=20,y=340)
    SenderID=Entry(main,width=25,fg="black",border=2,bg="white",font=("arial",15)).place(x=20,y=370)
    SenderID.focus()    
    
   
    Label(main,text="file name for incomiung file ",font=("arial",10,"bold"),bg="#f4fdfe").place(x=20,y=420)
    incoming_file=Entry(main,width=25,fg="black",border=2,bg="white",font=("arial",15)).place(x=20,y=450)
   

    imageicon=PhotoImage(file="images/send.png")##arrow
    
    rr=Button(main,text="Receive",compound=LEFT,image=imageicon,width=130,bg="#39c790",font="arial 14 bold",command=receiver)
    rr.place(x=20,y=500)
    main.mainloop()
    

#icon

image_icon=PhotoImage(file="images/icon.png")
root.iconphoto(False,image_icon)


Label(root,text="file transfer",font=("Acumin Variable Concept",20,"bold"),bg="#f4fdfe").place(x=20,y=30)

Frame(root,width=400,height=2,bg="#f2f5f6").place(x=25,y=80)


send_image=PhotoImage(file="images/send.png")
send=Button(root,image=send_image,bg="#f4fdfe",bd=0,command=Send)
send.place(x=50,y=100)
receive_image=PhotoImage(file="images/receive.png")
receive=Button(root,image=receive_image,bg="#f4fdfe",bd=0,command=Receive)
receive.place(x=300,y=100)
#label
Label(root,text="send",font=("Acumin Variable Concept",17,"bold"),bg="#f4fdfe").place(x=65,y=200)
Label(root,text="receive",font=("Acumin Variable Concept",17,"bold"),bg="#f4fdfe").place(x=300,y=200)
back_image=PhotoImage(file="images/send.png")
Label(root,image=back_image).place(x=65,y=323)

root.mainloop()











