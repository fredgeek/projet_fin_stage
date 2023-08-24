from tkinter import *
from tkinter import ttk

class all_spending:
    def __init__(self, root, width, height):
        self.fonts = ('Arial', 14, 'bold')
        self.width=width
        self.height=height
        ################# creation du canvas d'affichage ##################

        self.page = Canvas(root, width=self.width, height=self.height, bg="violet")
        # affichage du nombre d'évenements
        NbrFactureTraites=0
        NbrFactureNonTraites=0
        Label(self.page, text=f"vous avez {str(NbrFactureNonTraites)} factures non traités et {str(NbrFactureTraites)} factures en cours"
              , font=self.fonts, bg="#333333",fg="pink").place(x=20, y=4)

        #creation de notre treeview

        fenetre=ttk.Treeview(self.page,columns = (1,2,3,4,5),heigh=5, show = "headings")

        fenetre.heading(1,text="ID")
        fenetre.heading(2,text="payement/décaissement")
        fenetre.heading(3,text="date d'entrer")
        fenetre.heading(4,text="Montant")
        fenetre.heading(5,text="date de règlement")

        fenetre.column(1,width=50)
        fenetre.column(2,width=90)
        fenetre.column(3,width=50)
        fenetre.column(4,width=50)
        fenetre.column(5,width=50)


        fenetre.place(x=35,y=50,width=600,height=200)


        self.page.place(x=150, y=51)