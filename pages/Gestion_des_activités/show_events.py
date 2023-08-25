from tkinter import *
from tkinter import ttk
from tkinter.font import Font


class all_event:
    def __init__(self, root, width, height):
        self.fonts = ('Arial', 14, 'bold')
        self.width=width
        self.height=height
        ################# creation du canvas d'affichage ##################
        self.font = Font(family="Helvetica", size=12, underline=True, slant="italic", weight="bold")

        self.page = Canvas(root, width=self.width, height=self.height, bg="#333333")
        Label(self.page, text="3.       Consulter vos different rendez-vous.", font=self.font, bg="#333333",
              fg="pink").place(x=20, y=20)
        # affichage du nombre d'employer
        NbreEmployes=0
        Label(self.page, text=f"vous avez {str(NbreEmployes)} Rendez-vous.", font=self.fonts, bg="#333333",
              fg="pink").place(x=self.width-500, y=self.height-100)

        #creation de notre treeview

        fenetre=ttk.Treeview(self.page,columns = (1,2,3,4,5,6),heigh=5, show = "headings")

        fenetre.heading(1,text="ID")
        fenetre.heading(2,text="Date du RDV")
        fenetre.heading(3,text="Motif du RDV")
        fenetre.heading(4,text="Heur du RDV")
        fenetre.heading(5,text="Contact")
        fenetre.heading(6,text="sexe")



        fenetre.column(1,width=55)
        fenetre.column(2,width=55)
        fenetre.column(3,width=55)
        fenetre.column(4,width=55)
        fenetre.column(5,width=55)
        fenetre.column(6,width=55)


        fenetre.place(x=self.width/4,y=self.height/3,width=480,height=200)


        self.page.place(x=200, y=51)