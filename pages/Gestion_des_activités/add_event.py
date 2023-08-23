from tkinter import *
from tkinter import scrolledtext

from pages.home.home_page import HomePage

class New_event:
    def __init__(self,root,width,height):
        self.fonts = ('Arial',14,'bold')
        self.page = Canvas(root,width=width,height=height,bg="#333333")
        Label(self.page,text="Nouveau Rendez-vous. " ,font=self.fonts, bg="#333333",fg="pink" ).place(x=130,y=80)
        self.fonts = ('Arial',14,'bold')
        Label(self.page,text="De quel rendez-vous s'agit il ? le nom",font=self.fonts, bg="#333333",fg="pink" ).place(x=280,y=150)
        Entry(self.page,font=self.fonts,width=30).place(x=290,y=180)
        Label(self.page,text="Pour quand est programmer le rendez-vous?",font=self.fonts, bg="#333333",fg="pink" ).place(x=250,y=210)
        Entry(self.page,font=self.fonts,width=30).place(x=290,y=240)
        Label(self.page,text="Une petite description du rendez-vous",font=self.fonts, bg="#333333",fg="pink" ).place(x=280,y=270)
        scrolledtext.ScrolledText(self.page,width=38,height=4).place(x=290,y=300)
        Button(self.page,text="Enregistrer",font=self.fonts, bg="#333333",fg="cadetblue1",bd=0,activebackground="#333333").place(x=215,y=380)
        
        
        Button(self.page,font=self.fonts,text="Mes Rendez-vous",bg="#333333",fg="cadetblue1",bd=0,activebackground="#333333").place(x=540,y=450)
        
        Button(
            self.page, text="Go to home",
            command=lambda :HomePage(self.page, width=800, height=500),font=self.fonts, bg="#333333",fg="cadetblue1",bd=0,activebackground="#333333").place(x=540, y=380)
        self.page.place(x=0,y=0)