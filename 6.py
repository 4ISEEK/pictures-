from cProfile import label
import sqlite3
import datetime
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from base64 import b64encode as enc64
from base64 import b64decode as dec64
from io import BytesIO

global db
global sql
global u



db = sqlite3.connect('test3.db')

sql = db.cursor()
#________________________________________________
root = Tk()
root.title('Pictures')
root.geometry('600x600')
#root.resizable(width=False, height=False)
root['bg'] = 'white'
def next1():
    userloginsql = user_login.get()
    #userphonesql = user_phone.get()
    userpasswordsql = user_password.get()
    if userloginsql == '' or userpasswordsql == '':
        messagebox.showerror(title='Pictures', message='this field(s) null!')
    else:
        sql.execute(f"SELECT login FROM users WHERE login = '{userloginsql}'")
        if sql.fetchone() is None:
            sql.execute(f"INSERT INTO users VALUES(?, ?)", (userloginsql, userpasswordsql))
            db.commit()
            messagebox.showinfo(title='Pictures', message='Added!')
            login_window()
        else:
            messagebox.showerror(title='Pictures', message='this account already exists!')
            reg_window()
def singin1():
    global user_login2
    user_login2 = user_login1.get()
    user_password2 = user_password1.get()
    if user_login2 == "":
            messagebox.showerror(title='Pictures', message='empty filed login!')
    else:
        sql.execute(f'SELECT login FROM users WHERE login = "{user_login2}"')
        if sql.fetchone() is None:
            messagebox.showerror(title='Pictures', message='this account not found!')
            login_window()
        else:
            user_password2 = user_password1.get()
            sql.execute(f'SELECT "{user_login2}" FROM users WHERE password  = "{user_password2}"')
            if sql.fetchone() is None:
                messagebox.showerror(title='Pictures', message='pass error!')
                login_window()
            else:
                menu()
def reg1():
    reg_window()

def back1():
    login_window()

def login_window():
    global user_login1
    global user_password1
    frame = Frame(root, bg='white')
    frame.place(relwidth=1, relheight=1)

    main_label = Label(frame, text='SING IN', font='Arial 15 bold', bg='white', fg='black')
    username_label = Label(frame, text='login', font='Arial 11', bg='white', fg='gray')
    user_login1 = Entry(frame, font='Arial 11', bg='white', fg='black')
    userpassword_label = Label(frame, text='password', font='Arial 11', bg='white', fg='gray')
    user_password1 = Entry(frame, font='Arial 11', bg='white', fg='black')
    singin_button = Button(frame, text='SING IN', font='Arial 11', bg='black', fg='white', command=singin1)
    reg_button = Button(frame, text='REG IN', font='Arial 11', bg='black', fg='white', command=reg1)
    #___________________________________
    main_label.pack()
    username_label.pack()
    user_login1.pack()
    userpassword_label.pack()
    user_password1.pack()

    singin_button.pack(padx=10, pady=8)
    reg_button.pack(padx=10, pady=8)
    frame.mainloop()
    #_______

def reg_window():
    global user_login
   # global user_phone
    global user_password

    frame = Frame(root, bg='white')
    frame.place(relwidth=1, relheight=1)
    main_label = Label(frame, text='Creating account', font='Arial 15 bold', bg='white', fg='black')
    username_label = Label(frame, text='login', font='Arial 11', bg='white', fg='gray')
    user_login = Entry(frame, font='Arial 11', bg='white', fg='black')
    userpassword_label = Label(frame, text='password', font='Arial 11', bg='white', fg='gray')
    user_password = Entry(frame, font='Arial 11', bg='white', fg='black')
    next_button = Button(frame, text='Next', font='Arial 11', bg='black', fg='white', command=next1)
    back_button = Button(frame, text='Back', font='Arial 11', bg='black', fg='white', command=back1)
    #___________________________________
    main_label.pack()
    username_label.pack()
    user_login.pack()
    userpassword_label.pack()
    user_password.pack()
    next_button.pack(padx=10, pady=8)
    back_button.pack(padx=10, pady=8)
    frame.mainloop()

def menu(): 
    frame = Frame(root, bg='white')
    frame.place(relwidth=1, relheight=1)
    button_1 = Button(frame, text='1', font='Arial 11', bg='black', fg='white', command=p1)
    button_2 = Button(frame, text='2', font='Arial 11', bg='black', fg='white', command=p2)
    button_3 = Button(frame, text='3', font='Arial 11', bg='black', fg='white', command=p3)
    button_4 = Button(frame, text='4', font='Arial 11', bg='black', fg='white', command=p4)
    button_5 = Button(frame, text='5', font='Arial 11', bg='black', fg='white', command=p5)

    button_1.pack(padx=10, pady=8)
    button_2.pack(padx=10, pady=8)
    button_3.pack(padx=10, pady=8)
    button_4.pack(padx=10, pady=8)
    button_5.pack(padx=10, pady=8)
    frame.mainloop()

def p1():
    pic()

def p2():
    pic()

def p3():
    pic()

def p4(): 
    pic()

def p5():
    pic()

def pic():
    frame = Frame(root, bg='white')
    frame.place(relwidth=1, relheight=1)

    image = Image.open("1.png")
    photo = ImageTk.PhotoImage(image)
    label1 = Label(frame, image=photo)
    label1.pack()
    frame.mainloop()

def photo2():
    global img

    photos = sql.execute('SELECT photo FROM photos')
    k = 1
    for photo in photos:
        print(photo)
        img = dec64(photos)


    frame = Frame(root, bg='white')
    frame.place(relwidth=1, relheight=1)

    image = Image.open(img)
    photo = ImageTk.PhotoImage(image)
    label1 = Label(frame, image=photo)
    label1.pack()
    frame.mainloop()


photo2()
