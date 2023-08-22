from tkinter import *

from pages.home.home_page import HomePage


class RegisterPage:

    def __init__(self,root,width,height):
        # dimensions de la fenetre
        self.width = width
        self.height = height
        self.root = root

        # root = fenetre parent, width et height sont les dimensions de la fenetre
        self.page = Canvas(root,width=self.width,height=self.height,bg="green")
        Label(self.page,text="Register page").place(x=40,y=20)

        # bouton de transition ver le register_page
        #from pages.authentication.login_page import LoginPage
        #Button(
            #self.page, text="Se connecter",
            #command=lambda: LoginPage(self.page, width=self.width,height=self.height)).place(x=90, y=60)

        # bouton de transition ver le register_page approche 2
        Button(
        self.page, text="Se connecter",
        command=self.page.destroy).place(x=90, y=60)

        Button(
            self.page, text="Go to home",
            command=lambda :HomePage(self.page, width=800, height=500)).place(x=90, y=120)

        self.page.place(x=0,y=0)

