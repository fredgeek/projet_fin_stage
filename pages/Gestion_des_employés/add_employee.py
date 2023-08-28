from tkinter import *
from tkinter import messagebox as mb
from tkinter.font import Font

from tkinter import ttk
from tkinter import messagebox as mb
class ajout_employer :


    def __init__(self,root,width,height):
        self.width = width
        self.height = height
        self.fonts = ('Arial',14,'bold')
        self.page = Canvas(root,width=width,height=height,bg="#1978a5")
        self.font = Font(family="Helvetica", size=12, underline=True, slant="italic", weight="bold")
        Label(self.page,text="1.     Ajouter un nouvelle Employer " ,font=self.font, bg="#1978a5",fg="pink" ).place(x=20,y=20)

        Label(self.page,text="Entrer les informations de l'employer a enregistrer . "
              ,font=self.fonts, bg="#1978a5",fg="pink" ).place(x=130,y=80)
        Label(self.page,text="NOM : ",font=self.fonts, bg="#1978a5",fg="pink" ).place(x=200,y=150)
        Entry(self.page,font=self.fonts).place(x=280,y=150)
        Label(self.page,text="Email : ",font=self.fonts, bg="#1978a5",fg="pink" ).place(x=200,y=210)
        Entry(self.page,font=self.fonts).place(x=280,y=210)
        Label(self.page, text="TEL : ", font=self.fonts, bg="#1978a5", fg="pink").place(x=200, y=330)
        Entry(self.page, font=self.fonts).place(x=280, y=330)
        Label(self.page,text="Sexe : ",font=self.fonts, bg="#1978a5",fg="pink" ).place(x=200,y=260)
        i = IntVar()
        Radiobutton(self.page, text=" Homme ", value=1, variable=i, bg="#1978a5",activebackground="#1978a5",activeforeground="black").place(x=270, y=260)
        Radiobutton(self.page, text="Femme", value=2, variable=i, bg="#1978a5",activebackground="#1978a5",activeforeground="black").place(x=400, y=260)
        Button(self.page,text="Enregistrer",font=self.fonts, bg="blue",fg="cadetblue1"
               ,activebackground="#1978a5",activeforeground="blue",command=self.enregistre).place(x=215,y=450)
        Button(self.page,text="Liberez les champs ",font=self.fonts, bg="orange",fg="cadetblue1"
               ,activebackground="#1978a5",activeforeground="red",command=self.supprimer).place(x=415,y=450)

        
        
        #Button(
         #   self.page, text="Go to home",
          #  command=lambda :HomePage(self.page, width=800, height=500),font=self.fonts, bg="#333333",fg="cadetblue1").place(x=510, y=320)
        self.page.place(x=200,y=51)

    def enregistre(self):
            mb.askyesno("confirmer","vous confirmer que les informations entrez sont correctes? ")
    def supprimer(self):
        mb.askyesno("confirmer","Voulez- vous vraiment vider tous les champs ? ")
        self.page = Canvas(self.root,width=self.width,height=self.height,bg="#333333")
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
