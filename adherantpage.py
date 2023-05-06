import tkinter
import tkinter.ttk
import mysql.connector as mc
from tkinter import *
from tkinter import messagebox
import datetime
c=3
class Conn_livre():
    def __init__(self):
        self.host = "localhost"
        self.database = "user"
        self.user = "root"
        self.password = ""
        self.port = 3306
        self.conn = None
        self.cursor = None
        self.table = "livre"

    def connect(self):
        try:
            self.conn = mc.connect(host=self.host, database=self.database, user=self.user, password=self.password)
            print("connect to database")
        except mc.Error as err:
            print(err)
        self.cursor = self.conn.cursor()

    def disconnect(self):
        if self.cursor:
            self.cursor.close
        if self.conn:
            self.conn.close
    def getAll(self):
        req = f"select id,titre,auteur,annee_publication from {self.table} "
        self.cursor.execute(req)
        tasks = self.cursor.fetchall()
        return tasks
    def getAlladherant(self):
        req = f"select id,titre,auteur,annee_publication from {self.table} where reservation=0"
        self.cursor.execute(req)
        tasks = self.cursor.fetchall()
        return tasks
    def select_group(self,titre,auteur,annee_publication):
        req = f"select id,titre,auteur,annee_publication from {self.table} where titre like '{titre}%' and auteur like '{auteur}%' and annee_publication like '{annee_publication}%' "
        self.cursor.execute(req,)
        tasks = self.cursor.fetchall()
        return tasks
    def select_one(self,id):
        req = f"select * from {self.table} where id='%s'"
        values=(id,)
        self.cursor.execute(req,values)
        tasks = self.cursor.fetchall()
        return tasks
    def add(self, titre,auteur,annee_publication,image):
        req = f"insert into {self.table}(titre,auteur,annee_publication,image)values(%s,%s,%s,%s)"
        values = (titre,auteur,annee_publication,image)
        self.cursor.execute(req, values)
        self.conn.commit()
    def update(self, titre,auteur,annee_publication,image,id):
        req = f"update {self.table} set titre=%s , auteur=%s,annee_publication=%s,image=%s,reservation=0 where id=%s"
        values = (titre,auteur,annee_publication,image,id)
        self.cursor.execute(req, values)
        self.conn.commit()
    def update_res(self,id):
        req = f"update {self.table} set reservation=1  where id=%s"
        values = (id,)
        self.cursor.execute(req, values)
        self.conn.commit()
    def update_res_1(self,id):
        req = f"update {self.table} set reservation=0  where id=%s"
        values = (id,)
        self.cursor.execute(req, values)
        self.conn.commit()
    def delete(self, id):
        req = f"delete from {self.table} where id=%s"
        values = (id,)
        self.cursor.execute(req, values)
        self.conn.commit()

class reserves():
    def __init__(self):
        self.host = "localhost"
        self.database = "user"
        self.user = "root"
        self.password = ""
        self.port = 3306
        self.conn = None
        self.cursor = None
        self.table = "reservation"
    def connect(self):
        try:
            self.conn = mc.connect(host=self.host, database=self.database, user=self.user, password=self.password)
            print("connect to database")
        except mc.Error as err:
            print(err)
        self.cursor = self.conn.cursor()

    def disconnect(self):
        if self.cursor:
            self.cursor.close
        if self.conn:
            self.conn.close
    def reserve(self,id_livre,titre,nb_jours,auteur):
        req=f"insert into {self.table}(id_livre,titre,nb_jours,auteur,reservation)values(%s,%s,%s,%s,0)"
        values = (id_livre,titre,nb_jours,auteur)
        self.cursor.execute(req, values)
        self.conn.commit()
    def getAllres(self):
        req = f"select id_livre,titre,nb_jours from {self.table} where reservation=0"
        self.cursor.execute(req)
        tasks = self.cursor.fetchall()
        return tasks
    def select_one(self,id):
        req = f"select * from {self.table} where id_livre='%s'"
        values=(id,)
        self.cursor.execute(req,values)
        tasks = self.cursor.fetchall()
        return tasks
    def accepte(self,id,nb_jrs):
        data_livre_r = Conn_livre()
        data_livre_r.connect()
        data_livre_r.update_res(id)
        req = f"delete from {self.table} where id_livre=%s"
        values=(id,)
        self.cursor.execute(req,values)
        self.conn.commit()
        #after some days
        now = datetime.datetime.now()
        run_time = now + datetime.timedelta(days=nb_jrs)
        if datetime.datetime.now() == run_time:
        # traitement
             data_livre_r = Conn_livre()
             data_livre_r.connect()
             data_livre_r.update_res_1(id)
    def refuser(self,id):
        req = f"delete from {self.table} where id_livre=%s"
        values = (id,)
        self.cursor.execute(req, values)
        self.conn.commit()

def adherant_connected():
    #page config
    page_adherent=Tk()
    page_adherent.title('Gestion de Bibliotheque')
    page_adherent.geometry('1300x750+300+200')
    page_adherent.config(bg="#fff")
    page_adherent.resizable(False, False)
    page_adherent.iconbitmap('C:\\Users\\pc\\OneDrive\\Bureau\\PFA\\Books_icon-icons.com_76879.ico')
    # heading
    heading = Label(page_adherent, text="Gestion de la bibliothèque", fg="#57a1f8", bg="white", font=('NORMAL', 24, 'bold'))
    heading.place(x=520, y=5)
    #frame de rechere
    frame_rech=LabelFrame(page_adherent,text="Recherche",width=200,height=925,font=('NORMAL', 20, 'bold'),fg="#fff")
    frame_rech.config(bg="#57a1f8")
    frame_rech.place(x=0,y=0)
    #inputs de frame de recherche
    #input recherche par titre
    def on_enter(e):
        titre_rech.delete(0, 'end')

    def on_leave(e):
        titre = titre_rech.get()
        if titre == "":
            titre_rech.insert(0, "Titre de livre")
    titre_rech = Entry(frame_rech, width=15, fg="white", border=0, bg="#57a1f8", font=('NORMAL', 14))
    titre_rech.place(x=10, y=20)
    titre_rech.insert(0, "Titre de livre")
    titre_rech.bind('<FocusIn>', on_enter)
    titre_rech.bind('<FocusOut>', on_leave)
    f1 = Frame(frame_rech, width=180, height=2, bg='white')
    f1.place(x=5, y=47)
    #input recherche par auteur
    def on_enter(e):
        auteur_rech.delete(0, 'end')

    def on_leave(e):
        auteur = auteur_rech.get()
        if auteur == "":
            auteur_rech.insert(0, "Auteur du livre")
    auteur_rech = Entry(frame_rech, width=15, fg="white", border=0, bg="#57a1f8", font=('NORMAL', 14))
    auteur_rech.place(x=10, y=80)
    auteur_rech.insert(0, "Auteur du livre")
    auteur_rech.bind('<FocusIn>', on_enter)
    auteur_rech.bind('<FocusOut>', on_leave)
    f2 = Frame(frame_rech, width=180, height=2, bg='white')
    f2.place(x=5, y=107)

    # input recherche par annee
    def on_enter(e):
        annee_rech.delete(0, 'end')

    def on_leave(e):
        annee = annee_rech.get()
        if annee == "":
            auteur_rech.insert(0, "Année du livre")

    annee_rech = Entry(frame_rech, width=15, fg="white", border=0, bg="#57a1f8", font=('NORMAL', 14))
    annee_rech.place(x=10, y=140)
    annee_rech.insert(0, "Année du livre")
    annee_rech.bind('<FocusIn>', on_enter)
    annee_rech.bind('<FocusOut>', on_leave)
    f3 = Frame(frame_rech, width=180, height=2, bg='white')
    f3.place(x=5, y=167)

    def rechercher():
        if titre_rech.get() == "Titre de livre":
            titre_rech.delete(0, "end")
        if auteur_rech.get() == "Auteur du livre":
            auteur_rech.delete(0, "end")
        if annee_rech.get() == "Année du livre":
            annee_rech.delete(0, "end")
        table.delete(*table.get_children())
        datas = data_livre.select_group(titre_rech.get(), auteur_rech.get(), annee_rech.get())
        for row in datas:
            table.insert('', END, values=row)
        if titre_rech.get() == "":
            titre_rech.insert(0, "Titre de livre")
        if auteur_rech.get() == "":
            auteur_rech.insert(0, "Auteur du livre")
        if annee_rech.get() == "":
            annee_rech.insert(0, "Année du livre")

    # button de recherche
    btn1 = Button(frame_rech, width=15, text="Rechercher", pady=7, bg="white", fg="#57a1f8", border=0,
                  command=rechercher)
    btn1.place(x=40, y=227)
    #View
    table=tkinter.ttk.Treeview(page_adherent,columns=('ID','Titre','Auteur','Année'),show='headings')
    table.heading('ID',text='ID')
    table.heading('Titre', text='Titre')
    table.heading('Auteur', text='Auteur')
    table.heading('Année', text='Année de publication')
    table.column(0,width=50)
    table.place(x=400,y=100)
    data_livre=Conn_livre()
    data_livre.connect()
    datas=data_livre.getAlladherant()
    for row in datas:
        table.insert('',END,values=row)
        #Here, parent is the ID of the parent item that the new item should be added to. If parent is an empty string or None,
        # the new item will be added to the root level of the Treeview. index specifies the position where the new item should
        # be inserted under its parent. If index is set to 'end', the new item will be added to the end of the parent's children.




    #frame d'info sur livre
    frame_info = LabelFrame(page_adherent,text="Information sur le livre", width=700, height=350, font=('NORMAL', 20, 'bold'), fg="#57a1f8")
    frame_info.config(bg="white")
    frame_info.place(x=400,y=350)


    # fonction pour recuperer les données de la ligne selectionné
    def get_selection():
        try:
            selected_item = table.focus()
            details = table.item(selected_item)
            details_plus = details['values'][0]
            res = data_livre.select_one(details_plus)
            id_u = res[0][0]
            titre_u = res[0][1]
            auteur_u = res[0][2]
            annee_u = res[0][3]
            image_u = res[0][4]
            id_info_plus = Entry(frame_info, width=30, fg="black", border=0, bg="white", font=('NORMAL', 14))
            titre_info_plus = Entry(frame_info, width=30, fg="black", border=0, bg="white", font=('NORMAL', 14))
            auteur_info_plus = Entry(frame_info, width=30, fg="black", border=0, bg="white", font=('NORMAL', 14))
            annee_info_plus = Entry(frame_info, width=30, fg="black", border=0, bg="white", font=('NORMAL', 14))
            # Entry.insert(p1,p2):p1 est l'index de début de la chaine de caractére et p2 chaine de caractére
            id_info_plus.insert(0, f"ID : {id_u}")
            titre_info_plus.insert(0, f"Titre : {titre_u}")
            auteur_info_plus.insert(0, f"Auteur : {auteur_u}")
            annee_info_plus.insert(0, f"Année de pub : {annee_u}")

            id_info_plus.config(state=DISABLED)
            titre_info_plus.config(state=DISABLED)
            auteur_info_plus.config(state=DISABLED)
            annee_info_plus.config(state=DISABLED)
            id_info_plus.place(x=20, y=20)
            titre_info_plus.place(x=20, y=60)
            auteur_info_plus.place(x=20, y=100)
            annee_info_plus.place(x=20, y=140)
            print(image_u)
            #image du livre
            global  img_livre
            img_livre = PhotoImage(file=image_u)
            label_img_livre = Label(frame_info, image=img_livre, width=220, height=250)
            label_img_livre.place(x=400, y=10)
        except:
            messagebox.showerror("Erreur", "Il faut choisir un livre")
    def res():
        try:
            selected_item = table.focus()
            details = table.item(selected_item)
            details_plus = details['values'][0]
            res = data_livre.select_one(details_plus)
            id_u = res[0][0]
            titre_u = res[0][1]
            auteur_u = res[0][2]
        except:
            messagebox.showerror("Erreur", "Il faut choisir un livre")
        def ok(click1):
            print(click1)
            nb_jrs.destroy()
            res_livre = reserves()
            res_livre.connect()
            res_livre.reserve(id_u, titre_u, click1, auteur_u)

        nb_jrs=Tk()
        nb_jrs.title('Nombre de jours de réservation')
        nb_jrs.geometry('250x220')
        nb_jrs.config(bg="#fff")
        nb_jrs.resizable(False, False)
        nb_jrs.iconbitmap('C:\\Users\\pc\\OneDrive\\Bureau\\PFA\\Books_icon-icons.com_76879.ico')
        #dropDownList
        click=tkinter.IntVar()
        click.set(3)
        drop=OptionMenu(nb_jrs,click,3,7,15,30)
        drop.pack()
        c = click.get()
        btn_ok = Button(nb_jrs, width=20, text="Ok", pady=7, bg="black", fg="#57a1f8", border=0,command=lambda: ok(click.get()))
        btn_ok.place(x=50, y=180)








    # button pour plus d'information
    btn2 = Button(page_adherent, width=15, text="Plus Info", pady=7, bg="black", fg="#57a1f8", border=0, command=get_selection)
    btn2.place(x=580, y=300)
    btnResv= Button(page_adherent, width=15, text="Reserver", pady=7, bg="black", fg="#57a1f8", border=0,command=res)
    btnResv.place(x=780, y=300)

    page_adherent.mainloop()