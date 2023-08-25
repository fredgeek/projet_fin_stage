from tkinter import *
from tkinter import ttk

class Nbr_employer:
    def __init__(self, root, width, height):
        self.fonts = ('Arial', 14, 'bold')
        self.width=width
        self.height=height
        ################# creation du canvas d'affichage ##################

        self.page = Canvas(root, width=self.width, height=self.height, bg="violet")
        # affichage du nombre d'employer
        NbreEmployes=0
        Label(self.page, text=f"vous avez {str(NbreEmployes)} Employés", font=self.fonts, bg="#333333",
              fg="pink").place(x=20, y=4)

        #creation de notre treeview

        fenetre=ttk.Treeview(self.page,columns = (1,2,3),heigh=5, show = "headings")

        fenetre.heading(1,text="Nom")
        fenetre.heading(2,text="Prenom")
        fenetre.heading(3,text="Email")

        fenetre.column(1,width=50)
        fenetre.column(2,width=50)
        fenetre.column(3,width=50)


        fenetre.place(x=100,y=50,width=350,height=100)


        self.page.place(x=200, y=51)