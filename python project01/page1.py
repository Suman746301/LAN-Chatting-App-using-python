from tkinter import *
from tkinter import messagebox
import ast


########################
def signin():
    username=user.get()
    password=code.get()
    if (username=="admin" and password=="1234"):
        screen=Toplevel(root)
        screen.title("App")
        screen.geometry("925x500+300+200")
        screen.config(bg="white")
             
        Label(screen,text="hello i am shivraj", bg="#fff", font=("caliber(body)",50,"bold")).pack(expand=True)
    elif username!="admin" and password!="1234":
        messagebox.showerror("invalid","invalid username and password")
        
    elif username!="admin" :
        messagebox.showerror("invalid","invalid username")       
       
    elif password!="1234":
        messagebox.showerror("invalid","invalid  password")    


#############################
root=Tk()
root.title("Login")
root.geometry("1920x1080+300+200")
root.configure(bg="black")
root.resizable(True,True)

img=PhotoImage(file="login(00).png")
Label(root,image=img,bg="white").place(x=0,y=0)

frame=Frame(root,width=350,height=350,bg="white")

frame.place(x=600,y=260)

heading=Label(frame,text="SIGN IN" ,fg="#57a1f8",bg="white",font=('Montserrat',23,"bold"))

heading.place(x=100,y=5)


##################################
def on_enter(e):
    user.delete(0,"end")
    
def on_leave(e):
    name=user.get()
    if(name==" "):
        user.insert(0,"username")
        
    
    
    
user=Entry(frame,width=25,fg="black",border=0,bg="white",font=("Montserrat",11,"bold"))
user.place(x=30,y=80)
user.insert(0,"username")

user.bind("<FocusIn>",on_enter)
user.bind("<FocusOut>",on_leave)

Frame(frame,width=295,height=2,bg="black").place(x=25,y=107)

########################

def on_enter(e):
    code.delete(0,"end")
    
def on_leave(e):
    code=user.get()
    if(code==" "):
        code.insert(0,"password")

code=Entry(frame,width=25,fg="black",border=0,bg="white",font=("Montserrat",11,"bold"))
code.place(x=30,y=150)
code.insert(0,"password")

code.bind("<FocusIn>",on_enter)
code.bind("<FocusOut>",on_leave)



Frame(frame,width=295,height=2,bg="black").place(x=25,y=177)




#######################

Button(frame,width=39,pady=7,text="Sign in" ,font=("Montserrat",8,"bold"),fg="white",border=0,bg="#57a1f8",command=signin).place(x=25,y=204)
label=Label(frame,text="Don't have a account?" ,fg="black",bg="white",font=("Montserrat",9,"bold"))
label.place(x=75,y=270)

sign_up=Button(frame,width=6,text="Sign up" ,fg="#57a1f8",border=0,bg="white",cursor="hand2" ,font=("Montserrat",8,"bold"))
sign_up.place(x=215,y=270)






root.mainloop()