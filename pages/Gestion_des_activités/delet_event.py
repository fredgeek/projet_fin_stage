from tkinter import *
from tkinter.font  import Font
from tkinter import messagebox as mb
class delete_event :
    def __init__(self,root,width,height):
        self.fonts = ('Arial',14,'bold')
        self.page = Canvas(root,width=width,height=height,bg="#333333")
        self.font = Font(family="Helvetica", size=12, underline=True, slant="italic", weight="bold")
        Label(self.page, text="2.       Suppresion d'un rendez-vous.", font=self.font, bg="#333333",
              fg="pink").place(x=20, y=20)
        Label(self.page,text="Quel Rendez-vous voulez vous supprimer?. " ,font=self.fonts, bg="#333333",fg="pink" ).place(x=130,y=80)
        self.fonts = ('Arial',14,'bold')
        Label(self.page, text="Entrez l'identifiant du rendez-vous (NB: se renseigner dans la liste de vos Rendez-vous)"
              , font=self.fonts, bg="#333333", fg="pink").place(x=130, y=150)
        self.id=Entry(self.page, font=self.fonts)
        self.id.place(x=130, y=199)


        #Label(self.page, text="A quel heur etait le rende : ", font=self.fonts, bg="#333333", fg="pink").place(x=145, y=200)
        #Spinbox(self.page,from_=00, to=24, width=3).place(x=420, y=205)
        #Label(self.page,text="H",bg="#333333",fg="pink",width=1).place(x=450,y=205)
        #Spinbox(self.page, from_=00, to=60, width=3).place(x=465, y=205)
        #Label(self.page, text="Mins",width=3,bg="#333333",fg="pink").place(x=500,y=205)
        Button(self.page,text="Supprimmer ",font=self.fonts, bg="blue",fg="cadetblue1",command=self.enregistre).place(x=215,y=400)
        Button(self.page, text="vider le champ ", font=self.fonts, bg="orange", fg="cadetblue1"
               , command=self.supprimer, activebackground="#333333", activeforeground="red").place(x=415, y=400)

        #Button(s
         #   self.page, text="Go to home",
          #  command=lambda :HomePage(self.page, width=800, height=500),font=self.fonts, bg="#333333",fg="cadetblue1").place(x=510, y=320)
        self.page.place(x=200,y=51)

    def enregistre(self):
        mb.askyesno("confirmer", "vous confirmer que les informations entrez sont correctes? ")


    def supprimer(self):
        test=mb.askyesno("confirmer", "Voulez- vous vraiment vider tous les champs ? ")
        if test:
            self.id.delete(0,END)
