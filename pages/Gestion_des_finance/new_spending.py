from tkinter import *
from tkcalendar import *


class new_spending:

    def __init__(self,root,width,height):

        self.width = width
        self.height = height
############################   création du canvas d'affichage   ######################
        self.page = Canvas(self.page, width=self.width, height=self.height, bg="yellow")

        ############### creation du formulaire de renseignement ########################
        Label(self.page, text="Date d'entrer ",fg="black", font=("Arial",5,"bold"),bg="yellow").place(x=120,y=80)
        self.dat = DateEntry(self.page).placc(x=180,y=80)
        Label(self.page, text="Est-ce un payement ou un decaissement? ",fg="black", font=("Arial",5,"bold"),bg="yellow").place(x=120,y=120)
        Radiobutton(self.page)




#################################  affichage du canvas principale #####################
        self.page.place(x=150, y=51)
