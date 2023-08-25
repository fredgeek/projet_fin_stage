from tkinter import *
from tkinter import messagebox as mb
from tkinter.font import Font
class delete_employer :
    def __init__(self,root,width,height):
        self.fonts = ('Arial',14,'bold')
        self.page = Canvas(root,width=width,height=height,bg="#333333")
        self.font = Font(family="Helvetica", size=12, underline=True, slant="italic", weight="bold")
        Label(self.page,text="2.     Supprimer un employer " ,font=self.font, bg="#333333",fg="white" ).place(x=20,y=20)

        Label(self.page,text="Entrer les informations de l'employer a supprimer. " ,font=self.fonts, bg="#333333",fg="white" ).place(x=130,y=80)
        self.fonts = ('Arial',14,'bold')
        Label(self.page,text="NOM : ",font=self.fonts, bg="#333333",fg="pink" ).place(x=200,y=150)
        Entry(self.page,font=self.fonts).place(x=290,y=150)
        Label(self.page,text="Email : ",font=self.fonts, bg="#333333",fg="pink" ).place(x=200,y=240)
        Entry(self.page,font=self.fonts).place(x=290,y=240)
        Label(self.page, text="TEL : ", font=self.fonts, bg="#333333", fg="pink").place(x=200, y=330)
        Entry(self.page, font=self.fonts).place(x=280, y=330)


        Button(self.page, text="Supprimer", font=self.fonts, bg="#333333", fg="cadetblue1"
               ,activebackground="#333333",activeforeground="blue",command=self.enregistre).place(x=215, y=400)
        Button(self.page, text="liberez les champs ", font=self.fonts, bg="#333333", fg="cadetblue1"
               ,command=self.supprimer,activebackground="#333333",activeforeground="red").place(x=415, y=400)
        
        
        #Buttons
         #   self.page, text="Go to home",
          #  command=lambda :HomePage(self.page, width=800, height=500),font=self.fonts, bg="#333333",fg="cadetblue1").place(x=510, y=320)
        self.page.place(x=200,y=51)

    def enregistre(self):
        mb.askyesno("confirmer", "vous confirmer que les informations entrez sont correctes? ")

    def supprimer(self):
        mb.askyesno("confirmer", "Voulez- vous vraiment vider tous les champs ? ")