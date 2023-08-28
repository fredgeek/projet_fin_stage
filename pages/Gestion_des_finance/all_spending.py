from tkinter import *
from tkinter import ttk
from tkinter.font import Font

class all_spending:
    def __init__(self, root, width, height):
        self.fonts = ('Arial', 14, 'bold')
        self.width=width
        self.height=height
        ################# creation du canvas d'affichage ##################

        self.page = Canvas(root, width=self.width, height=self.height, bg="#05716c")
        self.font = Font(family="Helvetica", size=12, underline=True, slant="italic", weight="bold")
        Label(self.page, text="2.    Consulter la listes de vos factures ", fg="white", font=self.font, bg="#05716c").place(x=20, y=20)

        # affichage du nombre d'évenements
        NbrFactureTraites=0
        NbrFactureNonTraites=0
        Label(self.page, text=f"vous avez {str(NbrFactureNonTraites)} factures non traités et {str(NbrFactureTraites)} factures en cours"
              , font=self.fonts, bg="#05716c",fg="white").place(x=self.width-780, y=self.height-100)

        #creation de notre treeview

        fenetre=ttk.Treeview(self.page,columns = (1,2,3,4,5,6),heigh=5, show = "headings")

        fenetre.heading(1,text="ID")
        fenetre.heading(2,text="Encaissement/Décaissement")
        fenetre.heading(3,text="date d'entrer")
        fenetre.heading(4,text="Montant")
        fenetre.heading(5,text="Motif de la facture")
        fenetre.heading(6,text="Status")


        fenetre.column(1,width=50)
        fenetre.column(2,width=100)
        fenetre.column(3,width=50)
        fenetre.column(4,width=50)
        fenetre.column(5,width=50)
        fenetre.column(6,width=50)



        fenetre.place(x=100,y=200,width=600,height=200)


        self.page.place(x=200, y=51)