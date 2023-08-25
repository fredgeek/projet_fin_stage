from tkinter import *


class delete_employer :
    def __init__(self,root,width,height):
        self.fonts = ('Arial',14,'bold')
        self.page = Canvas(root,width=width,height=height,bg="#333333")
        Label(self.page,text="2.     Supprimer un employer " ,font=self.fonts, bg="#333333",fg="white" ).place(x=20,y=20)

        Label(self.page,text="Entrer les informations de l'employer a supprimer. " ,font=self.fonts, bg="#333333",fg="white" ).place(x=130,y=80)
        self.fonts = ('Arial',14,'bold')
        Label(self.page,text="NOM : ",font=self.fonts, bg="#333333",fg="pink" ).place(x=200,y=150)
        Entry(self.page,font=self.fonts).place(x=290,y=150)
        Label(self.page,text="Email : ",font=self.fonts, bg="#333333",fg="pink" ).place(x=200,y=240)
        Entry(self.page,font=self.fonts).place(x=290,y=240)
        Label(self.page, text="TEL : ", font=self.fonts, bg="#333333", fg="pink").place(x=200, y=330)
        Entry(self.page, font=self.fonts).place(x=280, y=330)
        Button(self.page, text="Enregistrer", font=self.fonts, bg="#333333", fg="cadetblue1",bd=0).place(x=215, y=400)
        Button(self.page, text="liberez les champs ", font=self.fonts, bg="#333333", fg="cadetblue1",bd=0).place(x=415, y=400)
        
        
        #Button(s
         #   self.page, text="Go to home",
          #  command=lambda :HomePage(self.page, width=800, height=500),font=self.fonts, bg="#333333",fg="cadetblue1").place(x=510, y=320)
        self.page.place(x=200,y=51)