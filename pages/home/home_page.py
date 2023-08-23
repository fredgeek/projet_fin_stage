from tkinter import *



class HomePage:
    def __init__(self,root,width,height):
        # dimensions de la fenetre
        self.width = width
        self.height = height

        # root = fenetre parent, width et height sont les dimensions de la fenetre
        self.page = Canvas(root,width=self.width,height=self.height,bg="yellow")

        #barre de presentation en haut
        self.presentationPart = Canvas(self.page,width=self.width,height=50,bg="#32a852")

        self.presentationPart.place(x=0,y=0)
        #fin de la barre de presentation

        from pages.authentication.login_page import LoginPage
        from pages.Gestion_des_employés.add_employee import ajout_employer
        from pages.Gestion_des_clients.Add_customer import ajout_client
        from pages.Gestion_des_activités.add_event import New_event
        from pages.Gestion_des_activités.delet_event import delet_event

        #menus des fonctionnalités
        self.fonction = Canvas(self.page,width=100,height=450,bg="blue")

        # creation du bouton mon compte
        Button(self.fonction, text=" Mon Compte", bg="blue"
               , width=13, height=1, fg="black",font=("arial",9,"italic")).place(x=4, y=12)

        #creation du menu des finances
        Button(self.fonction, text=" Finances "
               , bg="blue", width=13, height=1, fg="black",font=("arial",9,"italic")).place(x=4, y=130)
        #Menu1 = Menu(self.fonction, text=" Mes Employer "
            #   , bg="blue", width=13, height=1, fg="black",font=("arial",9,"italic")).place(x=4, y=40)
            
       #ajout du bouton employe
        Button(self.page, text=" Ajouter un employe ",fg="#fff",font=("arial",10),bg="#1c141f",bd=0,
               command = lambda:ajout_employer(self.page,self.width,self.height),activebackground="#1c141f").place(x=4,y=250)

        #creation du menu des evènements
        Button(self.fonction, text="Rendez-vous", bg="blue", width=13, height=1, fg="black",font=("arial",9,"italic")
               ,command = lambda:delet_event(self.page,self.width,self.height)).place(x=4, y=70)

        #creation du menus des clients
        Button(self.fonction, text=" Clients ", bg="blue", width=13, height=1, fg="black",font=("arial",9,"italic"),
               command = lambda:ajout_client(self.page,self.width,self.height)).place(x=4, y=100)
        #creation du menu des statistiques
        Button(self.fonction, text=" Statistiques "
               , bg="blue", width=13, height=1, fg="black", font=("arial", 9, "italic")).place(x=4, y=170)
        #creation du bouton se deconnecter
        Button(self.fonction, text=" SE Deconnecter ",bg="red",width=13,height=1,fg="black"
               ,command =lambda: LoginPage(self.page,self.width,self.height),font=("arial",9,"italic")).place(x=4,y=400)
        self.fonction.place(x=0,y=51)
        # fin de la barre des fonctionnalités

        #place de presentation des fonctionnalités
        self.present = Canvas(self.page,width=700,height=450,bg="aqua")




        self.present.place(x=100,y=51)
        #fin du menu de presentation des fnctionnalités


        #bouton de transition ver le register_page
       #  Button(
       #      self.page, text="Back button ",
       #         command=self.page.destroy).place(x=90,y=60)


        self.page.place(x=0,y=0)


