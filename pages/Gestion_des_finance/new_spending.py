from tkinter import *
from tkcalendar import *


class ajout_facture:

    def __init__(self,root,width,height):

        self.width = width
        self.height = height
############################   création du canvas d'affichage   ######################
        self.page = Canvas(root, width=self.width, height=self.height, bg="yellow")

        ############### creation du formulaire de renseignement ########################

        ############### entrer la date d'enregistrement de la facture ########################
        Label(self.page, text="Date d'entrer :",fg="black", font=("Arial",13,"bold"),bg="yellow").place(x=120,y=80)
        self.dat = DateEntry(self.page, bg="yellow").place(x=290,y=84)

        ############################## choisissez si c'est un encaissement ou un decaissement #######################
        Label(self.page, text="Est-ce un encaissement ou un decaissement? ",fg="black", font=("Arial",13,"bold"),bg="yellow").place(x=120,y=120)
        i=IntVar()
        Radiobutton(self.page, text="Encaissement",value=1,variable=i, bg="yellow").place(x=120,y=150)
        Radiobutton(self.page, text="Decaissement",value=2,variable=i, bg="yellow").place(x=240,y=150)

        ####################  entrer la date de payement si disponible ####################################
        Label(self.page, text="Date de payement(facultative) :", fg="black", font=("Arial",13, "bold"), bg="yellow").place(x=120, y=180)
        self.dat = DateEntry(self.page, bg="yellow").place(x=370, y=184)

        ################# entrez le montant de la facture ##################################
        Label(self.page, text="Entrer le montant de la facture ", fg="black", font=("Arial",13, "bold"), bg="yellow").place(x=120, y=230)
        Entry(self.page, font=("Arial",15,"bold"), bg="yellow").place(x=385,y=225)

        ############################### entrez un identifiant pour differencier les factures #############################
        Label(self.page, text="Entrer un identifiant pour la facture ", fg="black", font=("Arial",13, "bold"), bg="yellow").place(x=120, y=334)
        Entry(self.page, font=("Arial",15,"bold"), bg="yellow").place(x=425,y=325)

        ##################### bouton d'enregistrement #######################################

        Button(self.page,text="   Enregitrer   ",font=("Arial",10,"italic"),bd=0,fg="green").place(x=140,y=375)

#################################  affichage du canvas principale #####################
        self.page.place(x=200, y=51)
