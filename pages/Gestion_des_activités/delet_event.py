from tkinter import *

from pages.home.home_page import HomePage

class delet_event:
    def __init__(self,root,width,height):
        self.fonts = ('Arial',14,'bold')
        self.page = Canvas(root,width=width,height=height,bg="#333333")
        Label(self.page,text="supprimer un rendez-vous. " ,font=self.fonts, bg="#333333",fg="pink" ).place(x=130,y=80)
        Label(self.page,text="De quel rendez-vous s'agit il :",font=self.fonts, bg="#333333",fg="pink" ).place(x=200,y=150)
        Entry(self.page,font=self.fonts).place(x=500,y=150)
        Label(self.page,text="Quand etait il programmer : ",font=self.fonts, bg="#333333",fg="pink" ).place(x=200,y=225)
        Entry(self.page,font=self.fonts).place(x=500,y=225)
        Button(self.page,text="Supprimer",font=self.fonts, bg="#333333",fg="cadetblue1",bd=0,activebackground="#333333").place(x=215,y=310,)
        
        
        
        Button(
            self.page, text="Go to home",
            command=lambda :HomePage(self.page, width=800, height=500),font=self.fonts, bg="#333333",fg="cadetblue1",bd=0,activebackground="#333333").place(x=510, y=310)
        self.page.place(x=0,y=0)