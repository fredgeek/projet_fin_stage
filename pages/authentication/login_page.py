from tkinter import *

from pages.authentication.register_page import RegisterPage


class LoginPage:
    def __init__(self,root,width,height):
        # dimensions de la fenetre
        self.width = width
        self.height = height

        # partie de vos interfaces .....

        # root = fenetre parent, width et height sont les dimensions de la fenetre

        self.page = Canvas(root,width=width,height=height,bg="#1c141f")
        self.image = PhotoImage(file="login.png")
        Label(self.page, image=self.image,bg="#1c141f").place(x=30,y=150)


        #affichage de l image login avec ces caracteristiques
        Label(self.page,text=" Login ",fg="white",bg="#1c141f",font=("Arial",40)).place(x=500, y=30)

        # insertion de l'image ....


        # affichage de la l'entree username

        Label(self.page,text="Utilisateur :",fg="white",bg="#1c141f",font=("Arial",15)).place(x=600, y=180)
        username = Entry(self.page ,text="",font=("Arial",15,"bold"))
        username.place(x=760, y=180)

        #creation de la case password

        Label(self.page,text="Mot de passe :",fg="white",bg="#1c141f",font=("Arial",15)).place(x=600, y=275)
        username = Entry(self.page, text="", font=("Arial",15,"bold"),show="*")
        username.place(x=760, y=275)

        #Bouton dènregistrement des informations
        from pages.home.home_page import HomePage

        Button(self.page,text="                      Se connecter                  ",bg="#3711d1",font=("Arial",15,"bold"),fg="white",bd=0
               ,command=lambda :HomePage(self.page,self.width,self.height)).place(x=605,y=380)


        #demander a l'utilisateur si il a oublie son mot de passe

        Button(self.page, text=" Mot de passe oublie ? ",fg="#fff",font=("arial",13),bg="#1c141f",bd=0).place(x=745,y=317)
        Button(self.page, text=" Creer un compte ? ",fg="#fff",font=("arial",13),bg="#1c141f",bd=0,
               command = lambda: RegisterPage(self.page,self.width,self.height)).place(x=690,y=460)




        #bouton de transition ver le register_page
        #Button(
         #   self.page, text="S'inscrire",
          #     command=lambda: RegisterPage(self.page,width=self.width,height=self.height)).place(x=90,y=60)

        # fin de vos interfqaces .......
        self.page.place(x=0,y=0)










