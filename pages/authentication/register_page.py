from tkinter import *

from pages.home.home_page import HomePage


class RegisterPage:

    def __init__(self,root,width,height):
        self.fonts = ('Arial',14,'bold')
        # root = fenetre parent, width et height sont les dimensions de la fenetre
        self.page = Canvas(root,width=width,height=height,bg="#333333")
        Label(self.page,text="Sing-in . " ,font=self.fonts, bg="#333333",fg="pink" ).place(x=130,y=80)
        Label(self.page,text="NOM : ",font=self.fonts, bg="#333333",fg="pink" ).place(x=200,y=150)
        Entry(self.page,font=self.fonts).place(x=360,y=150)
        Label(self.page,text="PRENOM : ",font=self.fonts,bg="#333333",fg="pink").place(x=200,y=180)
        Entry(self.page,font=self.fonts).place(x=360,y=180)
        Label(self.page,text="E-MAIL : ",font=self.fonts, bg="#333333",fg="pink" ).place(x=200,y=210)
        Entry(self.page,font=self.fonts).place(x=360,y=210)
        Label(self.page,text="MOT DE PASS : ",font=self.fonts, bg="#333333",fg="pink" ).place(x=200,y=240)
        Entry(self.page,font=self.fonts).place(x=360,y=240)
        Label(self.page,text="GENRE : ",font=self.fonts, bg="#333333",fg="pink" ).place(x=200,y=270)
        Entry(self.page,font=self.fonts).place(x=360,y=270)
        Button(self.page,text="Enregistrer",font=self.fonts, bg="#333333",fg="cadetblue1",bd=0,activebackground="#333333").place(x=215,y=320)

        # bouton de transition ver le register_page
        #from pages.authentication.login_page import LoginPage
        #Button(
            #self.page, text="Se connecter",
            #command=lambda: LoginPage(self.page, width=800, height=500)).place(x=90, y=60)

        # bouton de transition ver le register_page approche 2
        Button(
        self.page, text="Se connecter",
        command=self.page.destroy,font=self.fonts, bg="#333333",fg="cadetblue1",bd=0,activebackground="#333333").place(x=355, y=320)

        Button(
            self.page, text="Go to home",
            command=lambda :HomePage(self.page, width=800, height=500),font=self.fonts, bg="#333333",fg="cadetblue1",bd=0,activebackground="#333333").place(x=510, y=320)

        self.page.place(x=0,y=0)

