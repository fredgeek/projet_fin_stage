from tkinter import *



class RegisterPage:

    def __init__(self,root,width,height):
        self.fonts = ('Arial',14,'bold')
        # root = fenetre parent, width et height sont les dimensions de la fenetre
        
        self.page = Canvas(root,width=width,height=height,bg="#1c141f")
        Label(self.page,text="Créez un compte. " ,font=self.fonts ,bg="#1c141f",fg="pink" ).place(x=240,y=80)
        Label(self.page,text="NOM : ",font=self.fonts,bg="#1c141f",fg="pink" ).place(x=400,y=160)
        nom=Entry(self.page,font=self.fonts).place(x=570,y=160)
        Label(self.page,text="PRENOM : ",font=self.fonts,bg="#1c141f",fg="pink").place(x=400,y=215)
        Entry(self.page,font=self.fonts).place(x=570,y=215)
        Label(self.page,text="E-MAIL : ",font=self.fonts,bg="#1c141f",fg="pink" ).place(x=400,y=265)
        Entry(self.page,font=self.fonts).place(x=570,y=265)
        Label(self.page,text="MOT DE PASS : ",font=self.fonts,bg="#1c141f",fg="pink" ).place(x=400,y=315)
        Entry(self.page,font=self.fonts).place(x=570,y=315)
        Label(self.page,text="GENRE : ",font=self.fonts,bg="#1c141f",fg="pink" ).place(x=400,y=370)
        Entry(self.page,font=self.fonts).place(x=570,y=370)
        
        Button(self.page,text="S'inscrire",font=self.fonts,bg="#1c141f",fg="cadetblue1",bd=0,).place(x=480,y=440)
        
            
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

