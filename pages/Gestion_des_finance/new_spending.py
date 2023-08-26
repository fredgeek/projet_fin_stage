from tkinter import *
from tkcalendar import *
from tkinter import messagebox as mb
from tkinter.font import Font

class ajout_facture:

    def __init__(self,root,width,height):

        self.width = width
        self.height = height
############################   création du canvas d'affichage   ######################
        self.page = Canvas(root, width=self.width, height=self.height, bg="yellow")
        self.font=Font(family="Helvetica",size=12,underline=True,slant="italic",weight="bold")
        Label(self.page, text="1.    Enregistrez les informations de votre facture", fg="black", font=self.font, bg="yellow").place(x=20, y=20)
        ############### creation du formulaire de renseignement ########################

        ############### entrer la date d'enregistrement de la facture ########################
        Label(self.page, text="Date d'entrer :",fg="black", font=("Arial",14,"bold"),bg="yellow").place(x=120,y=80)
        self.dat = DateEntry(self.page, bg="yellow").place(x=290,y=84)

        ############################## choisissez si c'est un encaissement ou un decaissement #######################
        Label(self.page, text="Est-ce un encaissement ou un décaissement? ",fg="black", font=("Arial",14,"bold"),bg="yellow").place(x=120,y=120)
        i=IntVar()
        Radiobutton(self.page, text="Encaissement",value=1,variable=i, bg="yellow",font=("Arial",12,"italic"),activebackground="yellow").place(x=120,y=150)
        Radiobutton(self.page, text="Décaissement",value=2,variable=i, bg="yellow",font=("Arial",12,"italic"),activebackground="yellow").place(x=280,y=150)
##################### bouton des facture traités et non traités ###############################
        Label(self.page, text="STATUS : ",fg="black", font=("Arial",14,"bold"),bg="yellow").place(x=120,y=180)
        j = IntVar()
        Radiobutton(self.page, text="Traité", value=1, variable=j, bg="yellow", font=("Arial", 12, "italic"),
                    activebackground="yellow").place(x=250, y=180)
        Radiobutton(self.page, text="Non Traité", value=2, variable=j, bg="yellow", font=("Arial", 12, "italic"),
                    activebackground="yellow").place(x=350, y=180)

        ####################  entrer la date de payement si disponible ####################################
        #Label(self.page, text="Date de payement(facultative) :", fg="black", font=("Arial",14, "bold"), bg="yellow").place(x=120, y=180)
        #self.dat = DateEntry(self.page, bg="yellow").place(x=450, y=184)

        ################# entrez le montant de la facture ##################################
        Label(self.page, text="Entrer le montant de la facture ", fg="black", font=("Arial",14, "bold"), bg="yellow").place(x=120, y=245)
        Entry(self.page, font=("Arial",14,"bold"), bg="yellow").place(x=425,y=245)

        ############################### entrez un identifiant pour differencier les factures #############################
        Label(self.page, text="Motif de la trancactions ", fg="black", font=("Arial",14, "bold"), bg="yellow").place(x=120, y=300)
        Entry(self.page, font=("Arial",14,"bold"), bg="yellow").place(x=425,y=300)

        ##################### bouton d'enregistrement et pour vider les champs #######################################

        Button(self.page,text="   Enregitrer   ",font=("Arial",14,"italic"),fg="green",
               bg="yellow",activebackground="yellow",activeforeground="blue",command=self.enregistre).place(x=225,y=375)
        Button(self.page, text="Liberez les champs ", font=("arial",14,"italic"), bg="yellow", fg="green",
               activebackground="yellow", activeforeground="red", command=self.supprimer).place(x=415, y=375)
################################  bouton pour modifier le status d'une facture ##############################
        Label(self.page, text="Pour modifier le status d'une factutre pré-enregistrez, cliquez ici : "
              , fg="black", font=("Arial",9, "bold"), bg="yellow").place(x=self.width/4 -60, y=self.height-100)

        Button(self.page, text="Modif.stat", font=("arial", 9, "italic"), bg="yellow", fg="green",
               activebackground="yellow", activeforeground="red").place(x=self.width/2 +40, y=self.height-100)

        #################################  affichage du canvas principale #####################
        self.page.place(x=200, y=51)

    def enregistre(self):
            mb.askyesno("confirmer","vous confirmer que les informations entrez sont correctes? ")
    def supprimer(self):
            mb.askyesno("confirmer","Voulez- vous vraiment vider tous les champs ? ")