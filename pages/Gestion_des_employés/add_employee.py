from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
class ajout_employer :


    def __init__(self,root,width,height):
        self.fonts = ('Arial',14,'bold')
        self.page = Canvas(root,width=width,height=height,bg="#333333")
        Label(self.page,text="1) Ajouter un nouvel employer " ,font=self.fonts, bg="#333333",fg="pink" ).place(x=50,y=20)

        Label(self.page,text="Entrer les informations de l'employer a enregistrer . " ,font=self.fonts, bg="#333333",fg="pink" ).place(x=130,y=80)
        Label(self.page,text="NOM : ",font=self.fonts, bg="#333333",fg="pink" ).place(x=200,y=150)
        self.nom=Entry(self.page,font=self.fonts).place(x=280,y=150)
        Label(self.page,text="Email : ",font=self.fonts, bg="#333333",fg="pink" ).place(x=200,y=210)
        self.email=Entry(self.page,font=self.fonts).place(x=280,y=210)
        Label(self.page, text="TEL : ", font=self.fonts, bg="#333333", fg="pink").place(x=200, y=270)
        self.tel=Entry(self.page, font=self.fonts).place(x=280, y=270)
        Button(self.page, text="Enregistrer", font=("Arial",14,"italic"), bg="#333333", fg="cadetblue1"
               , command=self.enregistre).place(x=350, y=340)
        Button(self.page,text="Effacer",font=("Arial",14,"italic"), bg="#333333",fg="cadetblue1"
               ,command=self.effacer).place(x=250,y=340)

        self.page.place(x=150, y=51)

    def  enregistre (self):
            mb.askyesno("sauvegarde", "vous confirmer que ces informations sont correctes?")



    def effacer(self):
        self.email.delete(0, END)
        self.nom.delete(0, END)
        self.tel.delete(0, END)
