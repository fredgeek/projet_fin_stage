from tkinter import *

from pages.authentication.register_page import RegisterPage


class LoginPage:
    def __init__(self,root,width,height):
        # dimensions de la fenetre
        self.width = width
        self.height = height

        # partie de vos interfaces .....

        # root = fenetre parent, width et height sont les dimensions de la fenetre
        self.page = Canvas(root,width=width,height=height,bg="#e48c4d")
        Label(self.page,text=" Login ",fg="#3711d1",bg="#e48c4d",font=("Arial",30)).place(x=270, y=20)

        # affichage de la l entree username

        Label(self.page,text="Username",fg="white",bg="#e48c4d",font=("Arial",15)).place(x=150, y=200)
        username = Entry(self.page ,text="",font=("Arial,30,bold"))
        username.place(x=250, y=200)

        #creation de la case password

        Label(self.page,text="Password",fg="white",bg="#e48c4d",font=("Arial",15)).place(x=150, y=300)
        username = Entry(self.page, text="", font=("Arial,30,bold"),show="*")
        username.place(x=250, y=300)

        #Bouton dènregistrement des informations

        Button(self.page,text=" Se connecter",bg="#3711d1",font=("Arial",13,"bold"),fg="white").place(x=250,y=370)


        #bouton de transition ver le register_page
        #Button(
         #   self.page, text="S'inscrire",
          #     command=lambda: RegisterPage(self.page,width=self.width,height=self.height)).place(x=90,y=60)

        # fin de vos interfqaces .......
        self.page.place(x=0,y=0)




