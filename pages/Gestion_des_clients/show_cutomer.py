from tkinter import *
from tkinter import ttk

class all_clients:
   def __init__(self, root, width, height):
        self.fonts = ('Arial', 14, 'bold')
        self.width=width
        self.height=height
        ################# creation du canvas d'affichage ##################

        self.page = Canvas(root, width=self.width, height=self.height, bg="violet")

        Label(self.page,text="3.     Consulter la liste de vos clients" ,font=self.fonts, bg="violet",fg="white" ).place(x=20,y=20)

        # affichage du nombre d'employer

        #creation de notre treeview

        fenetre=ttk.Treeview(self.page,columns = (1,2,3,4),heigh=5, show = "headings")

        fenetre.heading(1,text="Nom")
        fenetre.heading(2,text="Sexe")
        fenetre.heading(3,text="Tel")
        fenetre.heading(4,text="Email")

        fenetre.column(1,width=50)
        fenetre.column(2,width=50)
        fenetre.column(3,width=50)
        fenetre.column(4,width=50)


        Nbr_client=0
        Label(self.page, text=f"vous avez {str(Nbr_client)} clients", font=self.fonts, bg="violet",
              fg="white").place(x=self.width-500, y=self.height-110)

        fenetre.place(x=200,y=150,width=450,height=250)


        self.page.place(x=200, y=51)