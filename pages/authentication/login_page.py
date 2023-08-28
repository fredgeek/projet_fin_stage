from tkinter import *
from tkinter import messagebox as mb
from subprocess import call

from pages.authentication.register_page import RegisterPage

# creation de la class Loginpage
class LoginPage:
    def __init__(self,root,width,height):
        # dimensions de la fenetre
        self.width = width
        self.height = height
        # root = fenetre parent, width et height sont les dimensions de la fenetre
        
        #creation d'un canva de taille equale a la page Loginpage
        self.page = Canvas(root,width=width,height=height,bg="#1c141f")

        #affichage   du text login avec ces caracteristiques
        Label(self.page,text=" Login ",fg="#3711d1",bg="#1c141f",font=("Arial",30)).place(x=500, y=30)

        # affichage de la l'entree username

        username_label=Label(self.page,text="Username :",fg="white",bg="#1c141f",font=("Arial",15)).place(x=400, y=180)
        username = Entry(self.page ,font=("Arial,50,bold"))
        username.place(x=520, y=180)

        #creation de la case password

        password_label=Label(self.page,text="Password :",fg="white",bg="#1c141f",font=("Arial",15)).place(x=400, y=275)
        password = Entry(self.page, text="", font=("Arial,30,bold"),show="*")
        password.place(x=520, y=275)
        
        #creation de la fonction connection
        def connection():
               #test des entree
               if username.get()!="durel" and password.get()!="123":
                      mb.showwarning('Error','invalide entry')
               else:
                      mb.showinfo('sucsess','valide entry')
                      self.page.destroy
                      #une fois les information verifier on pass a la page d'acceuil
                      from pages.home.home_page import HomePage
                      call([HomePage(self.page,self.width,self.height)])
                      
                      

        #Bouton dènregistrement des informations
        

        Button(self.page,text=" Se connecter",bg="#3711d1",font=("Arial",14,"bold"),fg="white",bd=0
               ,command=connection).place(x=480,y=380)
       #  HomePage(self.page,self.width,self.height)


        #demander a l'utilisateur si il a oublie son mot de passe

        Button(self.page, text=" forget password? ",fg="#fff",font=("arial",10),bg="#1c141f",bd=0).place(x=440,y=460)
        Label(self.page, text="or",fg="#fff",font=("arial",10),bg="#1c141f",bd=0).place(x=550,y=463)
        Button(self.page, text=" Register? ",fg="#fff",font=("arial",10),bg="#1c141f",bd=0,
               command = lambda: RegisterPage(self.page,self.width,self.height)).place(x=564,y=460)

        self.page.place(x=0,y=0)




