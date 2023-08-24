from tkinter import *
from tkinter import ttk

class all_event:
    def __init__(self, root, width, height):
        self.fonts = ('Arial', 14, 'bold')
        self.width=width
        self.height=height
        ################# creation du canvas d'affichage ##################

        self.page = Canvas(root, width=self.width, height=self.height, bg="#333333")
        # affichage du nombre d'employer
        NbreEmployes=0
        Label(self.page, text=f"vous avez {str(NbreEmployes)} Employés", font=self.fonts, bg="#333333",
              fg="pink").place(x=20, y=7)

        #creation de notre treeview

        fenetre=ttk.Treeview(self.page,columns = (1,2,3),heigh=5, show = "headings")

        fenetre.heading(1,text="Lieu du RDV")
        fenetre.heading(2,text="Date du RDV")
        fenetre.heading(3,text="Heur du RDV")

        fenetre.column(1,width=55)
        fenetre.column(2,width=55)
        fenetre.column(3,width=55)
        
        fenetre.place(x=100,y=50,width=350,height=100)


        self.page.place(x=150, y=51)