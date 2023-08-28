from tkinter import *
from tkcalendar import *
from tkinter import messagebox as mb
from tkinter.font import Font

class ajout_facture:

    def __init__(self,root,width,height):

        self.width = width
        self.height = height
############################   création du canvas d'affichage   ######################
        self.page = Canvas(root, width=self.width, height=self.height, bg="#05716c")
        self.font=Font(family="Helvetica",size=12,underline=True,slant="italic",weight="bold")
        Label(self.page, text="1.    Enregistrez les informations de votre facture", fg="white", font=self.font, bg="#05716c").place(x=20, y=20)
        ############### creation du formulaire de renseignement ########################

        ############### entrer la date d'enregistrement de la facture ########################
        Label(self.page, text="Date d'entrer :",fg="white", font=("Arial",14,"bold"),bg="#05716c").place(x=120,y=80)
        self.dat = DateEntry(self.page, bg="#05716c")
        self.dat.place(x=290,y=84)

        ############################## choisissez si c'est un encaissement ou un decaissement #######################
        Label(self.page, text="Est-ce un encaissement ou un décaissement? ",fg="white", font=("Arial",14,"bold"),bg="#05716c").place(x=120,y=120)
        i=IntVar()
        Radiobutton(self.page, text="Encaissement",value=1,variable=i,activeforeground="white",activebackground="#05716c",fg="black", bg="#05716c",font=("Arial",14,"italic")).place(x=120,y=150)
        Radiobutton(self.page, text="Décaissement",value=2, variable=i,activeforeground="white",activebackground="#05716c",fg="black", bg="#05716c",font=("Arial",14,"italic")).place(x=280,y=150)
##################### bouton des facture traités et non traités ###############################
        Label(self.page, text="STATUS : ",fg="white", font=("Arial",14,"bold"),bg="#05716c").place(x=120,y=200)
        Radiobutton(self.page, text="Traité", value=1, variable=i,activebackground="#05716c",activeforeground="black",fg="black", bg="#05716c", font=("Arial", 12, "italic")
                    ).place(x=250, y=200)
        Radiobutton(self.page, text="Non Traité",value=2, variable=i,activebackground="#05716c",fg="black",activeforeground="white", bg="#05716c", font=("Arial", 12, "italic")
                    ).place(x=350, y=200)

        ####################  entrer la date de payement si disponible ####################################
        #Label(self.page, text="Date de payement(facultative) :", fg="black", font=("Arial",14, "bold"), bg="yellow").place(x=120, y=180)
        #self.dat = DateEntry(self.page, bg="yellow").place(x=450, y=184)

        ################# entrez le montant de la facture ##################################
        Label(self.page, text="Entrer le montant de la facture ", fg="black", font=("Arial",14, "bold"), bg="#05716c").place(x=120, y=245)
        Entry(self.page, font=("Arial",14,"bold")).place(x=425,y=245)

        ############################### entrez un identifiant pour differencier les factures #############################
        Label(self.page, text="Motif de la trancactions ", fg="black", font=("Arial",14, "bold"), bg="#05716c").place(x=120, y=300)
        Entry(self.page, font=("Arial",14,"bold")).place(x=425,y=300)

        ##################### bouton d'enregistrement et pour vider les champs #######################################

        Button(self.page,text="        Enregistrer        ",font=("Arial",14,"italic"),fg="white",
               bg="blue",activebackground="#05716c",activeforeground="blue",command=self.enregistre).place(x=215,y=375)
        Button(self.page, text="          Effacer          ", font=("arial",14,"italic"), bg="orange", fg="white",
               activebackground="#05716c", activeforeground="red", command=self.supprimer).place(x=430, y=375)
################################  bouton pour modifier le status d'une facture ##############################
        Label(self.page, text="Pour modifier le status d'une factutre pré-enregistrez, cliquez ici : "
              , fg="black", font=("Arial",9, "bold"), bg="#05716c").place(x=self.width/4 -60, y=self.height-100)

        Button(self.page, text="  Modif.stat  ", font=("arial", 9, "italic"), bg="blue", fg="white",
               activebackground="#05716c", activeforeground="red").place(x=self.width/2 +40, y=self.height-100)

        #################################  affichage du canvas principale #####################
        self.page.place(x=200, y=51)

    def enregistre(self):
            mb.askyesno("confirmer","vous confirmer que les informations entrez sont correctes? ")
    def supprimer(self):
            mb.askyesno("confirmer","Voulez- vous vraiment vider tous les champs ? ")