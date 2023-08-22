from tkinter import *

from pages.home.home_page import HomePage

class ajout_employer :
    def __init__(self,root,width,height):
        self.fonts = ('Arial',14,'bold')
        self.page = Canvas(root,width=width,height=height,bg="#333333")
        Label(self.page,text="entrer les information de l'employer a supprimer. " ,font=self.fonts, bg="#333333",fg="pink" ).place(x=130,y=80)
        self.fonts = ('Arial',14,'bold')
        Label(self.page,text="NOM : ",font=self.fonts, bg="#333333",fg="pink" ).place(x=200,y=150)
        Entry(self.page,font=self.fonts).place(x=360,y=150)
        Label(self.page,text="MOT DE PASS : ",font=self.fonts, bg="#333333",fg="pink" ).place(x=200,y=240)
        Entry(self.page,font=self.fonts).place(x=360,y=240)
        Button(self.page,text="Enregistrer",font=self.fonts, bg="#333333",fg="cadetblue1").place(x=215,y=320)
        
        
        
        Button(
            self.page, text="Go to home",
            command=lambda :HomePage(self.page, width=800, height=500),font=self.fonts, bg="#333333",fg="cadetblue1").place(x=510, y=320)
        self.page.place(x=0,y=0)