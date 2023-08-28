from tkinter import *
from tkinter.font import Font
from PIL import Image, ImageTk

class RegisterPage:

    def __init__(self, root, width, height):
        # dimensions de la fenetre
        self.fonts = ('Arial',14)
        self.width = width
        self.height = height

        # partie de vos interfaces .....

        # root = fenetre parent, width et height sont les dimensions de la fenetre

        self.page = Canvas(root, width=width, height=height, bg="#1c141f")
        self.image = PhotoImage(file="signup.png")
        Label(self.page, image=self.image, bg="#1c141f").place(x=30, y=150)

        Label(self.page,text="Créer un compte. " ,font=self.fonts ,bg="#1c141f",fg="pink" ).place(x=580,y=80)
        Label(self.page,text="NOM COMPLET : ",font=self.fonts,bg="#1c141f",fg="pink" ).place(x=580,y=160)
        nom=Entry(self.page,font=self.fonts)
        nom.place(x=790,y=160)
        Label(self.page,text="EMAIL : ",font=self.fonts,bg="#1c141f",fg="pink").place(x=580,y=215)
        Entry(self.page,font=self.fonts).place(x=790,y=215)
        Label(self.page,text="TELEPHONE : ",font=self.fonts,bg="#1c141f",fg="pink" ).place(x=580,y=265)
        Entry(self.page,font=self.fonts).place(x=790,y=265)
        Label(self.page,text="MOT DE PASS : ",font=self.fonts,bg="#1c141f",fg="pink" ).place(x=580,y=315)
        Entry(self.page,font=self.fonts).place(x=790,y=315)
        Label(self.page,text="GENRE : ",font=self.fonts,bg="#1c141f",fg="pink" ).place(x=580,y=370)
        Entry(self.page,font=self.fonts).place(x=790,y=370)
        
        Button(self.page,text="         Effacer         ",font=self.fonts,bg="orange",fg="white",bd=0,).place(x=580,y=440)
        
            
        Button(self.page,text="        S'inscrire        ",font=self.fonts,bg="blue",fg="white",bd=0,
            ).place(x=829,y=440)
        
        
        
        Button(self.page, text=" Vous avez un compte? ",fg="#fff",font=("arial",13),bg="#1c141f",bd=0,
               command=self.page.destroy).place(x=700,y=500)

        # bouton de transition ver le register_page
        #from pages.authentication.login_page import LoginPage
        #Button(
            #self.page, text="Se connecter",
            #command=lambda: LoginPage(self.page, width=800, height=500)).place(x=90, y=60)

        # bouton de transition ver le register_page approche 2
        
        self.page.place(x=0,y=0)

