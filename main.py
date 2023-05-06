from tkinter import *
from user import *
from adherantpage import *
from adminpage import *
from tkinter import messagebox
import user as us
root=Tk()
#screen size
root.title('Login')
root.geometry('925x500+300+200')
root.config(bg="#fff")
root.resizable(False,False)
root.iconbitmap('C:\\Users\\pc\\OneDrive\\Bureau\\PFA\\Books_icon-icons.com_76879.ico')
#image\
img=PhotoImage(file='c.jpg')
label_img=Label(root,image=img,width=350,height=350,bg="white")
label_img.place(x=50,y=50)
#frame
frame=Frame(root,width=350,height=350,bg="white")
frame.place(x=480,y=70)
#heading
heading=Label(frame,text="S'authentifier",fg="#57a1f8",bg="white",font=('NORMAL',24,'bold'))
heading.place(x=100,y=5)
#inputs

def on_enter(e):
    username.delete(0,'end')
def on_leave(e):
    name=username.get()
    if name=="":
        username.insert(0,"Nom d'utilisateur")


username=Entry(frame,width=25,fg="black",border=0,bg="white",font=('NORMAL',14))
username.place(x=80,y=80)
username.insert(0,"Nom d' utilisateur")
username.bind('<FocusIn>',on_enter)
username.bind('<FocusOut>',on_leave)

f1=Frame(frame,width=295,height=2,bg='black')
f1.place(x=75,y=107)
#--------------
def on_enter(e):
    password.delete(0,'end')
def on_leave(e):
    pwd=password.get()
    if pwd=="":
        password.insert(0,'Mot de passe')
password=Entry(frame,width=25,fg="black",border=0,bg="white",font=('NORMAL',14))
password.place(x=80,y=150)
password.insert(0,"Mot de passe")
password.bind('<FocusIn>',on_enter)
password.bind('<FocusOut>',on_leave)
f2=Frame(frame,width=295,height=2,bg='black')
f2.place(x=75,y=177)
#verifier les infos
def verify():
    c=Adherent(username.get(),password.get())
    c.connect()
    a=c.verify(username.get(),password.get())
    print(a)
    if a==2:
        messagebox.showinfo("","admin")
        root.destroy()
        admin_connected()

    elif a==1:
        messagebox.showinfo("", "adherant")
        root.destroy()
        adherant_connected()
    else:
        messagebox.showerror("Erreur","Nom utilisateur ou le mot de passe sont incorrects")
#button
btn=Button(frame,width=30,text="s'authentifier",pady=7,bg="#57a1f8",fg="white",border=0,command=verify)
btn.place(x=105,y=210)
#-------
#register page
def return_conn():


    def register():
        #title and frame
        heading1.destroy()
        frame1.destroy()
        frame = Frame(root, width=350, height=350, bg="white")
        frame.place(x=480, y=70)
        heading = Label(frame, text="S'authentifier", fg="#57a1f8", bg="white", font=('NORMAL', 24, 'bold'))
        heading.place(x=100, y=5)
        # button pour se render a la page de connection
        label2.destroy()
        btn_conn.destroy()
        label1 = Label(frame, text="vous n'avez pas de compte ?", fg="black", bg="white", font=(9))
        label1.place(x=105, y=270)
        btn_eng = Button(frame, width=30, text="creer un compte", pady=7, fg="black", border=0,command=return_conn)
        btn_eng.place(x=105, y=310)
        #reverifier les infos
        def reverify():
            c = Adherent(username.get(), password.get())
            c.connect()
            a = c.verify(username.get(), password.get())
            print(a)
            if a == 2:
                messagebox.showinfo("", "admin")
                root.destroy()
                admin_connected()

            elif a == 1:
                messagebox.showinfo("", "adherant")
                root.destroy()
                adherant_connected()
            else:
                messagebox.showerror("Erreur", "Nom utilisateur ou le mot de passe sont incorrects")
        # button enregistrer
        btn1.destroy()
        btn = Button(frame, width=30, text="s'authentifier", pady=7, bg="#57a1f8", fg="white", border=0,command=reverify)
        btn.place(x=105, y=210)
        # inputs
        username1.destroy()
        f11.destroy()
        password1.destroy()
        f21.destroy()
        reinput_password.destroy()
        f3.destroy()

        def on_enter(e):
            username.delete(0, 'end')

        def on_leave(e):
            name = username.get()
            if name == "":
                username.insert(0, "Nom d'utilisateur")

        username = Entry(frame, width=25, fg="black", border=0, bg="white", font=('NORMAL', 14))
        username.place(x=80, y=80)
        username.insert(0, "Nom d' utilisateur")
        username.bind('<FocusIn>', on_enter)
        username.bind('<FocusOut>', on_leave)

        f1 = Frame(frame, width=295, height=2, bg='black')
        f1.place(x=75, y=107)

        # --------------
        def on_enter(e):
            password.delete(0, 'end')

        def on_leave(e):
            pwd = password.get()
            if pwd == "":
                password.insert(0, 'Mot de passe')

        password = Entry(frame, width=25, fg="black", border=0, bg="white", font=('NORMAL', 14))
        password.place(x=80, y=150)
        password.insert(0, "Mot de passe")
        password.bind('<FocusIn>', on_enter)
        password.bind('<FocusOut>', on_leave)
        f2 = Frame(frame, width=295, height=2, bg='black')
        f2.place(x=75, y=177)


    # title and frame
    heading.destroy()
    frame.destroy()
    frame1 = Frame(root, width=350, height=400, bg="white")
    frame1.place(x=480, y=30)
    heading1 = Label(frame1, text="S'enregistrer", fg="#57a1f8", bg="white", font=('NORMAL', 24, 'bold'))
    heading1.place(x=100, y=0)
    # button pour se render a la page de connection
    label1.destroy()
    btn_eng.destroy()
    label2 = Label(frame1, text="voulez vous se connecter ?", fg="black", bg="white", font=(9))
    label2.place(x=105, y=320)
    btn_conn = Button(frame1, width=30, text="se connecter", pady=7, fg="black", border=0,command=register)
    btn_conn.place(x=105, y=360)

    #inputs

    username.destroy()
    f1.destroy()
    password.destroy()
    f2.destroy()

    # username
    def on_enter(e):
        username1.delete(0, 'end')

    def on_leave(e):
        name1 = username1.get()
        if name1 == "":
            username1.insert(0, "Entrer le nom d' utilisateur")

    username1 = Entry(frame1, width=25, fg="black", border=0, bg="white", font=('NORMAL', 13))
    username1.place(x=80, y=60)
    username1.insert(0, "Entrer le nom d' utilisateur")
    username1.bind('<FocusIn>', on_enter)
    username1.bind('<FocusOut>', on_leave)
    f11 = Frame(frame1, width=295, height=2, bg='black')
    f11.place(x=75, y=87)
    #password
    def on_enter(e):
        password1.delete(0, 'end')

    def on_leave(e):
        pwd1 = password1.get()
        if pwd1 == "":
            password1.insert(0, 'Entrer un  mot de passe')

    password1 = Entry(frame1, width=25, fg="black", border=0, bg="white", font=('NORMAL', 13))
    password1.place(x=80, y=130)
    password1.insert(0, "Entrer un  mot de passe")
    password1.bind('<FocusIn>', on_enter)
    password1.bind('<FocusOut>', on_leave)
    f21 = Frame(frame1, width=295, height=2, bg='black')
    f21.place(x=75, y=150)
    #reinput password
    def on_enter(e):
        reinput_password.delete(0, 'end')

    def on_leave(e):
        rpwd = reinput_password.get()
        if rpwd == "":
            reinput_password.insert(0, 'Confirmer le  mot de passe')

    reinput_password = Entry(frame1, width=25, fg="black", border=0, bg="white", font=('NORMAL', 13))
    reinput_password.place(x=80, y=197)
    reinput_password.insert(0, "Confirmer le  mot de passe")
    reinput_password.bind('<FocusIn>', on_enter)
    reinput_password.bind('<FocusOut>', on_leave)
    f3 = Frame(frame1, width=295, height=2, bg='black')
    f3.place(x=75, y=224)

    # function of register
    def register_adherant():
        if(password1.get()==reinput_password.get()):
            user = Adherent(username1.get(),password1.get())
            user.connect()
            user.insert()
            user.disconnect()
            a=messagebox.showinfo("Félicitation","votre compte est créer")
            if a=="ok":
                register()

        else:
            messagebox.showwarning("mot de passe","le mot de passe ne correspond pas")

    #button enregistrer
    btn.destroy()
    btn1 = Button(frame1, width=30, text="enregistrer", pady=7, bg="#57a1f8", fg="white", border=0,command=register_adherant)
    btn1.place(x=105, y=260)
label1=Label(frame,text="vous n'avez pas de compte ?",fg="black",bg="white",font=(9))
label1.place(x=105,y=270)
btn_eng=Button(frame,width=30,text="creer un compte",pady=7,fg="black",border=0,command=return_conn)
btn_eng.place(x=105,y=310)


root.mainloop()