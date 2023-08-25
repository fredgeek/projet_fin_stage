from tkinter import *


class ajout_employer :
    def __init__(self,root,width,height):
        self.fonts = ('Arial',14,'bold')
        self.page = Canvas(root,width=width,height=height,bg="#333333")
        Label(self.page,text="1.     Ajouter un nouvelle Employer " ,font=self.fonts, bg="#333333",fg="pink" ).place(x=20,y=20)

        Label(self.page,text="Entrer les informations de l'employer a enregistrer . " ,font=self.fonts, bg="#333333",fg="pink" ).place(x=130,y=80)
        Label(self.page,text="NOM : ",font=self.fonts, bg="#333333",fg="pink" ).place(x=200,y=150)
        Entry(self.page,font=self.fonts).place(x=280,y=150)
        Label(self.page,text="Email : ",font=self.fonts, bg="#333333",fg="pink" ).place(x=200,y=210)
        Entry(self.page,font=self.fonts).place(x=280,y=210)
        Label(self.page, text="TEL : ", font=self.fonts, bg="#333333", fg="pink").place(x=200, y=330)
        Entry(self.page, font=self.fonts).place(x=280, y=330)
        Label(self.page,text="Sexe : ",font=self.fonts, bg="#333333",fg="pink" ).place(x=200,y=260)
        i = IntVar()
        Radiobutton(self.page, text="Homme", value=1, variable=i, bg="#333333",activebackground="#333333").place(x=270, y=260)
        Radiobutton(self.page, text="Femme", value=2, variable=i, bg="#333333",activebackground="#333333").place(x=400, y=260)
        Button(self.page,text="Enregistrer",font=self.fonts, bg="#333333",fg="cadetblue1",bd=0).place(x=215,y=450)
        Button(self.page,text="Liberez les champs ",font=self.fonts, bg="#333333",fg="cadetblue1",bd=0).place(x=415,y=450)

        
        
        #Button(
         #   self.page, text="Go to home",
          #  command=lambda :HomePage(self.page, width=800, height=500),font=self.fonts, bg="#333333",fg="cadetblue1").place(x=510, y=320)
        self.page.place(x=200,y=51)