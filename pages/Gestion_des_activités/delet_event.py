from tkinter import *


class delete_event :
    def __init__(self,root,width,height):
        self.fonts = ('Arial',14,'bold')
        self.page = Canvas(root,width=width,height=height,bg="#333333")
        Label(self.page,text="Quel Rendez-vous voulez vous supprimer?. " ,font=self.fonts, bg="#333333",fg="pink" ).place(x=130,y=80)
        self.fonts = ('Arial',14,'bold')
        Label(self.page, text="Lieu du rendez-vous : ", font=self.fonts, bg="#333333", fg="pink").place(x=145, y=150)
        Entry(self.page, font=self.fonts).place(x=400, y=150)
        Label(self.page, text="A quel heur etait le rende : ", font=self.fonts, bg="#333333", fg="pink").place(x=145, y=200)
        Spinbox(self.page,from_=00, to=24, width=3).place(x=420, y=205)
        Label(self.page,text="H",bg="#333333",fg="pink",width=1).place(x=450,y=205)
        Spinbox(self.page, from_=00, to=60, width=3).place(x=465, y=205)
        Label(self.page, text="Mins",width=3,bg="#333333",fg="pink").place(x=500,y=205)
        Button(self.page,text="Supprimmer ",font=self.fonts, bg="#333333",fg="cadetblue1").place(x=215,y=320)
        
        
        
        #Button(s
         #   self.page, text="Go to home",
          #  command=lambda :HomePage(self.page, width=800, height=500),font=self.fonts, bg="#333333",fg="cadetblue1").place(x=510, y=320)
        self.page.place(x=200,y=51)