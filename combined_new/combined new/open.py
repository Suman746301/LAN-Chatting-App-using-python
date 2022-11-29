from tkinter import *
from tkinter import messagebox
import ast
import smtplib
import random

root=Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False,False)

###################
def signin():
    username=user.get()
    password=code.get()

    file=open('datasheet.txt','r+')
    d=file.read()
    r=ast.literal_eval(d)
    file.close()

    #print(r.keys())
    #print(r.values())
    
    # finding ussename and password in file

    if username in r.keys() and password==r[username]:
        screen=Toplevel(root)
        screen.title("App")
        screen.geometry('925x500+300+200')
        screen.config(bg="white")

        Label(screen,text='Hello Everyone!',bg='#fff', font=('Calibri(Body',50,'bold')).pack(expand=True)

        #screen.mainloop()
        #print('Yes it is I')
        '''elif username!='admin' and password!='1234':
        messagebox.showerror("Invalid","Invalid username and password")

        elif password!="1234":
            messagebox.showerror("Invalid","Invalid password")'''
    else:
        messagebox.showerror("Invalid","Invalid Username or password")

##if new login is done
    
def signup_command():
    window=Toplevel(root)
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
                window.destroy()
                
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

    heading=Label(frame,text='Sign up',fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light',23,'bold'))
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
                user.insert(0,'E-mail')

    user= Entry(frame,width=30,fg='black', border=2,bg="white",font=('Microsoft YaHei UI Light', 11))
    user.place(x=60, y=70)
    user.insert(0,'E-mail')
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


# forget password command


def forget_command(username):
    window=Toplevel(root)
    window.title("SignUp")
    window.geometry('925x500+300+200')
    window.configure(bg='#fff')
    window.resizable(False,False)
 ###############################################################
    ## function to send the otp
            
    # creates SMTP session
    
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login("suaravsuman991@gmail.com", "pajytmtqnsitrfea")

    # message to be sent
    message = random.randint(1,9)*102207
    otp_send=message
    print(otp_send)
    # sending the mail
    s.sendmail("suaravsuman991@gmail.com", "itssuman7463@gmail.com", str(otp_send))

    # terminating the session
    s.quit()

    ############################
    def reset():
        OTP=otp.get()
        if otp_send==int(OTP):
            messagebox.showinfo('OK',"OTP validated")
        else:
            messagebox.showerror('Invalid',"Wrong OTP")
    

    ### if we click signin then signup should close
    def sign():
        password=code.get()
        conform_password=conform_code.get()
        if password==conform_password:
            try:
                file=open('datasheet.txt','r+')
                d=file.read()
                r=ast.literal_eval(d)

                #dict2={username:password}
                r.update({username:password})
                #r.update(dict2)
                file.truncate(0)
                file.close()

                file=open('datasheet.txt','w')
                w=file.write(str(r))

                messagebox.showinfo('Done','Successfully Changed')
                window.destroy()
            
        ###if file is not present then it will create file
            except:
                file=open('datasheet.txt','w')
                pp=str({'Username':'password'})
                file.write(pp)
                file.close()  

        else:
            messagebox.showerror('Invalid',"Both Password should match")
        #window.destroy()

    img=PhotoImage(file='login.png')
    Label(window,image=img,bg='white').place(x=50,y=50)

    #placing the login icon on the page
    frame=Frame(window,width=450,height=280,bg="white")
    frame.place(x=480,y=70)

    heading=Label(frame,text='Reset Password',fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light',21,'bold'))
    heading.place(x=70,y=5)  

    ######################

    '''def on_enter(e):
        user.delete(0, 'end')

    def on_leave(e):
            name=user.get()
            if name=='':
                user.insert(0,'Username')

    user= Entry(frame,width=30,fg='black', border=2,bg="white",font=('Microsoft YaHei UI Light', 11))
    user.place(x=60, y=70)
    user.insert(0,'Username')
    user.bind('<FocusIn>', on_enter)
    user.bind('FocusOut', on_leave)'''

    ###################

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
        otp.delete(0, 'end')

    def on_leave(e):
            name=otp.get()
            if name=='':
                otp.insert(0,'OTP')

    otp= Entry(frame,width=30,fg='black', border=2,bg="white",font=('Microsoft YaHei UI Light', 11))
    otp.place(x=60, y=70)
    otp.insert(0,'OTP')
    otp.bind('<FocusIn>', on_enter)
    otp.bind('FocusOut', on_leave)

    ###########################
    def on_enter(e):
        code.delete(0, 'end')

    def on_leave(e):
            name=code.get()
            if name=='':
                code.insert(0,'New Password')

    code= Entry(frame,width=30,fg='black', border=2,bg="white",font=('Microsoft YaHei UI Light', 11))
    code.place(x=60, y=120)
    code.insert(0,'New Password')
    code.bind('<FocusIn>', on_enter)
    code.bind('FocusOut', on_leave)

    #############################
    sign_in= Button(frame, width=0, text='', border=0, bg='white', cursor='hand2',fg='#57a1f8', command=reset)
    sign_in.place(x=215, y=98)

    Button(frame, width=25,pady=6,text='Done ', bg='#57a1f8', fg='white', border=0,command=sign).place(x=95, y=220)
    #label=Label(frame,text="I have an accout?", fg='black', bg='white',font=('Microsoft YaHei UI Light', 9))
    #label.place(x=105, y=220)

    #sign_in= Button(frame, width=6, text='Sign in', border=0, bg='white', cursor='hand2',fg='#57a1f8',command=sign)
    #sign_in.place(x=215, y=300)

    window.mainloop()

######################################3
def reset_send_otp():
    window=Toplevel(root)
    window.title("Password Reset")
    window.geometry('925x500+300+200')
    window.configure(bg='#fff')
    window.resizable(False,False)

    #####################
    def signup():
        username=user.get()
        file=open('datasheet.txt','r+')
        d=file.read()
        r=ast.literal_eval(d)
        file.close()
        
        if username in r.keys():
            pass
        else:
            messagebox.showerror('Invalid',"User name not found!")     
        return username

    def sign():
        window.destroy()
    
    def send_user():
        username=signup()
        forget_command(username)

    img=PhotoImage(file='login.png')
    Label(window,image=img,bg='white').place(x=50,y=50)

    #placing the login icon on the page
    frame=Frame(window,width=450,height=250,bg="white")
    frame.place(x=480,y=70)

    heading=Label(frame,text='Reset Password',fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light',21,'bold'))
    heading.place(x=70,y=5) 

    def on_enter(e):
         user.delete(0, 'end')

    def on_leave(e):
            name=user.get()
            if name=='':
                user.insert(0,'E-mail')

    user= Entry(frame,width=30,fg='black', border=2,bg="white",font=('Microsoft YaHei UI Light', 11))
    user.place(x=60, y=70)
    user.insert(0,'E-mail')
    user.bind('<FocusIn>', on_enter)
    user.bind('FocusOut', on_leave)  
 
    Button(frame, width=22,pady=6,text='Continue ', bg='#57a1f8', fg='white', border=0,command=send_user).place(x=90, y=120)
    #label=Label(frame,text="I have an accout?", fg='black', bg='white',font=('Microsoft YaHei UI Light', 9))
    #label.place(x=60, y=100)

    sign_in= Button(frame, width=6, text='Back', border=0, bg='white', cursor='hand2',fg='#57a1f8',command=sign)
    sign_in.place(x=250, y=125)

    # sign_in= Button(frame, width=8, text='Send OTP', border=0, bg='white', cursor='hand2',fg='#57a1f8', command=reset)
    # sign_in.place(x=215, y=98)

    window.mainloop()
##adding image to the login page

img=PhotoImage(file='login.png')
Label(root,image=img,bg='white').place(x=50,y=50)

#placing the login icon on the page
frame=Frame(root,width=350,height=350,bg="white")
frame.place(x=480,y=70)

heading=Label(frame,text='Sign in',fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=115,y=5)


def on_enter(e):
    user.delete(0, 'end')

def on_leave(e):
        name=user.get()
        if name=='':
            user.insert(0,'E-mail')

user= Entry(frame,width=30,fg='black', border=2,bg="white",font=('Microsoft YaHei UI Light', 11))
user.place(x=60, y=70)
user.insert(0,'E-mail')
user.bind('<FocusIn>', on_enter)
user.bind('FocusOut', on_leave)

#Frame(frame,width=295,bg='black').place(x=25,y=107)
def on_enter(e):
    code.delete(0, 'end')

def on_leave(e):
        name=user.get()
        if name=='':
            code.insert(0,'Password')

code= Entry(frame,width=30,fg='black', border=2,bg="white",font=('Microsoft YaHei UI Light', 11))
code.place(x=60, y=130)
code.insert(0,'Password')
code.bind('<FocusIn>', on_enter)
code.bind('FocusOut', on_leave)

#######################

Button(frame, width=25,pady=6,text='Sign in', bg='#57a1f8', fg='white', border=0,command=signin).place(x=95, y=200)
label=Label(frame,text="Don't have an accout?", fg='black', bg='white',font=('Microsoft YaHei UI Light', 9))
label.place(x=98, y=250)

forget_password= Button(frame, width=20, text='Forget password!', border=0, bg='white', cursor='hand2',fg='#57a1f8',command=reset_send_otp)
forget_password.place(x=160, y=160)

sign_up= Button(frame, width=6, text='Sign up', border=0, bg='white', cursor='hand2',fg='#57a1f8',command=signup_command)
sign_up.place(x=227, y=250)


root.mainloop()

            
