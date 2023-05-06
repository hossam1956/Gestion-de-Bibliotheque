import tkinter.ttk
from tkinter import filedialog
import mysql.connector as mc
from tkinter import *
from tkinter import messagebox
from adherantpage import *
import adherantpage
def admin_connected():
    page_admin = Tk()
    page_admin.title('Gestion de Bibliotheque')
    page_admin.geometry('1300x750+300+200')
    page_admin.config(bg="#fff")
    page_admin.resizable(False, False)
    page_admin.iconbitmap('C:\\Users\\pc\\OneDrive\\Bureau\\PFA\\Books_icon-icons.com_76879.ico')

    #heading
    heading = Label(page_admin, text="Gestion de la bibliothèque", fg="#57a1f8", bg="white",font=('NORMAL', 24, 'bold'))
    heading.place(x=520, y=5)

    lbl1 = Label(page_admin, text="Nom du livre:", font=30, bg="#57a1f8")
    lbl1.place(x=350, y=100)
    e1 = Entry(page_admin, width=60)
    e1.place(x=600, y=100)
    lbl2 = Label(page_admin, text="Auteur:", font=10, bg="#57a1f8")
    lbl2.place(x=350, y=150)
    e2 = Entry(page_admin, width=60)
    e2.place(x=600, y=150)
    lbl3 = Label(page_admin, text="Date de Publication:", font=20, bg="#57a1f8")
    lbl3.place(x=350, y=200)
    e3 = Entry(page_admin, width=60)
    e3.place(x=600, y=200)
    lbl4 = Label(page_admin, text="Image:", font=20, bg="#57a1f8")
    lbl4.place(x=350, y=250)
    #fonction d'imporation d'image

    def import_img():
        global path_img1
        path_img=filedialog.askopenfile(initialdir="C:/Users/pc/OneDrive/Bureau/PFA/img",title="selectionner une image",filetypes=(("png files","*.png"),("gif files","*.gif")))
        path_img1=path_img.name

    btn4 = Button(page_admin, text="Importer une image", width=60, bg="white",fg="#57a1f8",command=import_img)
    btn4.place(x=600, y=250)

    # objet de Conn_livre
    data_livre = Conn_livre()
    data_livre.connect()
    #table treview

    tree = tkinter.ttk.Treeview(page_admin, columns=(1, 2, 3, 4), height=5, show="headings")
    tree.place(x=300, y=420, width=800, height=275)
    tree.heading(1, text="ID")
    tree.heading(2, text="Titre")
    tree.heading(3, text="Auteur")
    tree.heading(4, text="Date de publication")

    tree.column(1, width=50)

    tree.column(2, width=100)
    tree.column(3, width=100)
    datas = data_livre.getAll()
    for row in datas:
        tree.insert('', END, values=row)


    def Ajouter():

        data_livre.add(e1.get(),e2.get(),e3.get(),path_img1)
        messagebox.showinfo("Info","Livre est ajoutée")
        # delete pour supprimer tous les éléments de la TreeView
        #la méthode get_children pour obtenir la liste de tous les éléments de la TreeView.
        #La méthode * est utilisée pour déballer la liste et passer chaque élément comme argument à la méthode 'delete'
        tree.delete(*tree.get_children())
        datas = data_livre.getAll()
        for row in datas:
            tree.insert('', END, values=row)
        e1.delete(0, 'end')
        e2.delete(0, 'end')
        e3.delete(0, 'end')
    def supprimer():
        try:
            selected_item = tree.focus()
            details = tree.item(selected_item)
            details_plus = details['values'][0]
            res = data_livre.select_one(details_plus)
            id_u = res[0][0]
            data_livre.delete(id_u)
            messagebox.showinfo("Info", "Livre est supprimé")
            tree.delete(*tree.get_children())
            datas = data_livre.getAll()
            for row in datas:
                tree.insert('', END, values=row)
        except:
            messagebox.showerror("Erreur", "Il faut choisir un livre")

    def quitter():
        a=messagebox.askyesno("Quitter","Voulez vous quitter ?")
        if(a==True):
            data_livre.disconnect()
            page_admin.destroy()
    def modifier():
        try:
            selected_item = tree.focus()
            details = tree.item(selected_item)
            details_plus = details['values'][0]
            res = data_livre.select_one(details_plus)
            id_u = res[0][0]
            titre_u = res[0][1]
            auteur_u = res[0][2]
            annee_u = res[0][3]
            page_modif=Tk()
            page_modif.title('Modifier')
            page_modif.geometry('700x400+300+200')
            page_modif.config(bg="#fff")
            page_modif.resizable(False, False)
            page_modif.iconbitmap('C:\\Users\\pc\\OneDrive\\Bureau\\PFA\\Books_icon-icons.com_76879.ico')
            #heading modifier
            heading = Label(page_modif, text="Modifier", fg="#57a1f8", bg="white",font=('NORMAL', 20, 'bold'))
            heading.place(x=10, y=5)
            #inputs
            lbl1m = Label(page_modif, text="Nom du livre:", font=10, bg="#57a1f8")
            lbl1m.place(x=10, y=60)
            e1m = Entry(page_modif, width=60)
            e1m.place(x=200, y=60)
            e1m.insert(END,titre_u)
            lbl2m = Label(page_modif, text="Auteur:", font=10, bg="#57a1f8")
            lbl2m.place(x=10, y=110)
            e2m = Entry(page_modif, width=60)
            e2m.insert(END, auteur_u)
            e2m.place(x=200, y=110)
            lbl3m = Label(page_modif, text="Date de Publication:", font=10, bg="#57a1f8")
            lbl3m.place(x=10, y=160)
            e3m = Entry(page_modif, width=60)
            e3m.insert( END, annee_u)
            e3m.place(x=200, y=160)
            lbl4m = Label(page_modif, text="Image:", font=20, bg="#57a1f8")
            lbl4m.place(x=10, y=210)
            btn4m = Button(page_modif, text="Importer une image", width=60, bg="white", fg="#57a1f8", command=import_img)
            btn4m.place(x=200, y=210)
            def modif():
                data_livre.update(e1m.get(),e2m.get(),e3m.get(),path_img1,id_u)
                messagebox.showinfo("Info", "Livre est modifié")
                tree.delete(*tree.get_children())
                datas = data_livre.getAll()
                for row in datas:
                    tree.insert('', END, values=row)
                page_modif.destroy()
            #button de modif
            btnM = Button(page_modif, text="Modifier", width=20, bg="#57a1f8", command=modif)
            btnM.place(x=250, y=250)

            page_modif.mainloop()
        except:
            messagebox.showerror("Erreur", "Il faut choisir un livre")
    def Resv():
        page_Resv = Tk()
        page_Resv.title('Reservation des livres')
        page_Resv.geometry('700x400+300+200')
        page_Resv.config(bg="#fff")
        page_Resv.resizable(False, False)
        page_Resv.iconbitmap('C:\\Users\\pc\\OneDrive\\Bureau\\PFA\\Books_icon-icons.com_76879.ico')
        # table treview

        tree_Resv = tkinter.ttk.Treeview(page_Resv, columns=(1, 2, 3), height=5, show="headings")
        tree_Resv.place(x=50, y=10, width=600, height=250)
        tree_Resv.heading(1, text="ID_livre")
        tree_Resv.heading(2, text="Titre")
        tree_Resv.heading(3, text="Nb de jours")

        data_res=reserves()
        data_res.connect()
        data_res1 = data_res.getAllres()
        for row in data_res1:
            tree_Resv.insert('', END, values=row)
        #choisir une reservation

        def ch_res_accep():

            selected_item = tree_Resv.focus()
            details = tree_Resv.item(selected_item)
            details_plus = details['values'][0]
            res = data_res.select_one(details_plus)
            id_u = res[0][0]
            data_res.accepte(id_u,adherantpage.c)
            page_Resv.destroy()


        def ch_res_refu():
            try:
                selected_item = tree_Resv.focus()
                details = tree_Resv.item(selected_item)
                details_plus = details['values'][0]
                res = data_res.select_one(details_plus)
                id_u = res[0][0]
                data_res.refuser(id_u)
                page_Resv.destroy()
            except:
                messagebox.showerror("Erreur", "Il faut choisir un livre")

        btnAcp = Button(page_Resv, text="Accepter ", width=20, bg="#57a1f8",command=ch_res_accep)
        btnAcp.place(x=120, y=300)
        btnRef = Button(page_Resv, text="Refuser ", width=20, bg="#57a1f8",command=ch_res_refu)
        btnRef.place(x=420, y=300)






    btnResv = Button(page_admin, text="Reservation", width=20, bg="#57a1f8",command=Resv)
    btnResv.place(x=250, y=350)
    btn1 = Button(page_admin, text="Ajouter", width=20, bg="#57a1f8",command=Ajouter)
    btn1.place(x=450, y=350)
    btn2 = Button(page_admin, text="Supprimer", width=20, bg="#57a1f8",command=supprimer)
    btn2.place(x=650, y=350)
    btn3 = Button(page_admin, text="Modifier", width=20, bg="#57a1f8",command=modifier)
    btn3.place(x=850, y=350)
    btn4 = Button(page_admin, text="Quitter", width=20, bg="#57a1f8",command=quitter)
    btn4.place(x=1050, y=350)



    #--------------------------------
    #Partie Recherche
    # frame de rechere
    frame_rech = LabelFrame(page_admin, text="Recherche", width=200, height=925, font=('NORMAL', 20, 'bold'), fg="#fff")
    frame_rech.config(bg="#57a1f8")
    frame_rech.place(x=0, y=0)

    # inputs de frame de recherche
    # input recherche par titre
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

    # input recherche par auteur
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

    #----------------------
    def rechercher():
        if titre_rech.get()=="Titre de livre":
            titre_rech.delete(0, "end")
        if auteur_rech.get() == "Auteur du livre":
             auteur_rech.delete(0, "end")
        if annee_rech.get() == "Année du livre":
             annee_rech.delete(0, "end")
        tree.delete(*tree.get_children())
        datas = data_livre.select_group(titre_rech.get(),auteur_rech.get(),annee_rech.get())
        for row in datas:
            tree.insert('', END, values=row)
        if titre_rech.get()=="":
            titre_rech.insert(0, "Titre de livre")
        if auteur_rech.get() == "":
             auteur_rech.insert(0, "Auteur du livre")
        if annee_rech.get() == "":
             annee_rech.insert(0, "Année du livre")






    # button de recherche
    btn1 = Button(frame_rech, width=15, text="Rechercher", pady=7, bg="white", fg="#57a1f8", border=0,command=rechercher)
    btn1.place(x=40, y=227)

    page_admin.mainloop()
