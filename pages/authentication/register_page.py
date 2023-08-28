from tkinter import *
from tkinter import ttk
from subprocess import call
from tkinter import messagebox as mb


class RegisterPage:

    def __init__(self,root,width,height):
        self.fonts = ('Arial',14,'bold')
        # root = fenetre parent, width et height sont les dimensions de la fenetre
        
        self.page = Canvas(root,width=width,height=height,bg="#1c141f")
        Label(self.page,text="Créez un compte. " ,font=self.fonts ,bg="#1c141f",fg="pink" ).place(x=240,y=80)
        
        #nom
        Label(self.page,text="NOM : ",font=self.fonts,bg="#1c141f",fg="pink" ).place(x=400,y=160)
        nom=Entry(self.page,font=self.fonts)
        nom.place(x=570,y=160)
        
        #prenom
        Label(self.page,text="PRENOM : ",font=self.fonts,bg="#1c141f",fg="pink").place(x=400,y=215)
        prenom=Entry(self.page,font=self.fonts)
        prenom.place(x=570,y=215)
        
        #email
        Label(self.page,text="E-MAIL : ",font=self.fonts,bg="#1c141f",fg="pink" ).place(x=400,y=265)
        email=Entry(self.page,font=self.fonts)
        email.place(x=570,y=265)
        
        #mot de pass
        Label(self.page,text="MOT DE PASS : ",font=self.fonts,bg="#1c141f",fg="pink" ).place(x=400,y=315)
        mot_pass=Entry(self.page,font=self.fonts)
        mot_pass.place(x=570,y=315)
        
        #sex
        Label(self.page,text="GENRE : ",font=self.fonts,bg="#1c141f",fg="pink" ).place(x=400,y=370)
        sex=ttk.Combobox(self.page,font=self.fonts,state='readonly')
        sex["values"]=("Homme","Femme")
        sex.current(0)
        sex.place(x=570,y=370,width=200)
        
        def inscrire():
            self.page.destroy()
            # from pages.authentication.login_page import LoginPage
            # call([LoginPage(self.page, width=800, height=500)])
            mb.showinfo('Enregistre.','Vos information on bient été enregitré.')
        
        #  bouton d'inscription
        Button(self.page,text="S'inscrire",font=self.fonts,bg="#1c141f",fg="cadetblue1",bd=0,command=inscrire).place(x=480,y=440)
        
            
        Button(self.page,text="Effacer tout",font=self.fonts,bg="#1c141f",fg="cadetblue1",bd=0,
            ).place(x=630,y=440)
        
        
        
        Button(self.page, text=" Vous avez un compte? ",fg="#fff",font=("arial",10),bg="#1c141f",bd=0,
               command=self.page.destroy).place(x=480,y=500)

        # bouton de transition ver le register_page
        #from pages.authentication.login_page import LoginPage
        #Button(
            #self.page, text="Se connecter",
            #command=lambda: LoginPage(self.page, width=800, height=500)).place(x=90, y=60)

        # bouton de transition ver le register_page approche 2
        
        self.page.place(x=0,y=0)

