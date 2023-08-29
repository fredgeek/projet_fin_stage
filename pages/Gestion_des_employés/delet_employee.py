from tkinter import *
from tkinter import messagebox as mb
from tkinter.font import Font
class delete_employer :
    def __init__(self,root,width,height):
        self.fonts = ('Arial',14,'bold')
        self.page = Canvas(root,width=width,height=height,bg="#1978a5")
        self.font = Font(family="Helvetica", size=12, underline=True, slant="italic", weight="bold")
        Label(self.page,text="2.     Supprimer un employer " ,font=self.font, bg="#1978a5",fg="white" ).place(x=20,y=20)

        Label(self.page,text="Entrer les informations de l'employer a supprimer. " ,font=self.fonts, bg="#1978a5",fg="white" ).place(x=130,y=80)
        self.fonts = ('Arial',14,'bold')
        Label(self.page,text="NOM : ",font=self.fonts, bg="#1978a5",fg="white" ).place(x=200,y=150)
        self.nom=Entry(self.page,font=self.fonts)
        self.nom.place(x=290,y=150)
        Label(self.page,text="Email : ",font=self.fonts, bg="#1978a5",fg="white" ).place(x=200,y=240)
        self.email=Entry(self.page,font=self.fonts)
        self.email.place(x=290,y=240)
        Label(self.page, text="TEL : ", font=self.fonts, bg="#1978a5", fg="white").place(x=200, y=330)
        self.tel=Entry(self.page, font=self.fonts)
        self.tel.place(x=280, y=330)


        Button(self.page, text="Supprimer", font=self.fonts, bg="blue", fg="cadetblue1"
               ,activebackground="#1978a5",activeforeground="blue",command=self.enregistre).place(x=215, y=400)
        Button(self.page, text="vider le champs ", font=self.fonts, bg="orange", fg="cadetblue1"
               ,command=self.supprimer,activebackground="#1978a5",activeforeground="red").place(x=415, y=400)
        
        
        #Buttons
         #   self.page, text="Go to home",
          #  command=lambda :HomePage(self.page, width=800, height=500),font=self.fonts, bg="#333333",fg="cadetblue1").place(x=510, y=320)
        self.page.place(x=200,y=51)

    def enregistre(self):
        mb.askyesno("confirmer", "vous confirmer que les informations entrez sont correctes? ")

    def supprimer(self):
        test=mb.askyesno("confirmer", "Voulez- vous vraiment vider tous les champs ? ")
        if test:
            self.email.delete(0,END)
            self.nom.delete(0,END)
            self.tel.delete(0,END)
