from tkinter import *

from pages.authentication.register_page import RegisterPage
from pages.Gestion_des_employés.add_employee import ajout_employer


class LoginPage:
    def __init__(self,root,width,height):
        # root = fenetre parent, width et height sont les dimensions de la fenetre
        self.page = Canvas(root,width=width,height=height,bg="#333333")
        Label(self.page,text="Login page").place(x=40,y=20)

        #bouton de transition ver le register_page
        Button(
            self.page, text="S'inscrire",
               command=lambda: RegisterPage(self.page,width=800,height=500)).place(x=90,y=60)
        Button(
            self.page, text="ajouter un employer",
               command=lambda: ajout_employer(self.page,width=800,height=500)).place(x=90,y=100)


        self.page.place(x=0,y=0)


