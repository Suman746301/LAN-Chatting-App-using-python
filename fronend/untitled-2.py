from tkinter import *
from tkinter import messagebox
import ast

window=Tk()
window.title("SignUp")
window.geometry('925x500+300+200')
window.configure(bg='#fff')
window.resizable(False,False)

def signup():
    username=user.get()
    password=code.get()
    conform_password=conform_code.get()

    if password==conform_password:
        try:
            file=open('datasheet.txt','r+')
            d=file.read()
            r=ast.literal_eval(d)

            dict2={username:password}
            r.update(dict2)
            file.truncate(0)
            file.close()

            file=open('datasheet.txt','w')
            w=file.write(str(r))

            messagebox.showinfo('Signup','Successfully sign up')

        ###if file is not present then it will create file
        except:
            file=open('datasheet.txt','w')
            pp=str({'Username':'password'})
            file.write(pp)
            file.close()

    else:
        messagebox.showerror('Invalid',"Both Password should match")        

### if we click signin then signup should close
def sign():
    window.destroy()

img=PhotoImage(file='login.png')
Label(window,image=img,bg='white').place(x=50,y=50)

#placing the login icon on the page
frame=Frame(window,width=450,height=350,bg="white")
frame.place(x=480,y=70)

heading=Label(frame,text='Sign in',fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=115,y=5)

######################

def on_enter(e):
    conform_code.delete(0, 'end')

def on_leave(e):
        name=conform_code.get()
        if name=='':
           conform_code.insert(0,'Conform Password')

conform_code= Entry(frame,width=30,fg='black', border=2,bg="white",font=('Microsoft YaHei UI Light', 11))
conform_code.place(x=60, y=170)
conform_code.insert(0,'Conform Password')
conform_code.bind('<FocusIn>', on_enter)
conform_code.bind('FocusOut', on_leave)

###############################
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

###########################
def on_enter(e):
    code.delete(0, 'end')

def on_leave(e):
        name=code.get()
        if name=='':
            code.insert(0,'Password')

code= Entry(frame,width=30,fg='black', border=2,bg="white",font=('Microsoft YaHei UI Light', 11))
code.place(x=60, y=120)
code.insert(0,'Password')
code.bind('<FocusIn>', on_enter)
code.bind('FocusOut', on_leave)

#############################
Button(frame, width=25,pady=6,text='Sign up', bg='#57a1f8', fg='white', border=0, command=signup).place(x=95, y=220)
label=Label(frame,text="I have an accout?", fg='black', bg='white',font=('Microsoft YaHei UI Light', 9))
label.place(x=105, y=260)

sign_in= Button(frame, width=6, text='Sign in', border=0, bg='white', cursor='hand2',fg='#57a1f8',command=sign)
sign_in.place(x=215, y=260)

window.mainloop()