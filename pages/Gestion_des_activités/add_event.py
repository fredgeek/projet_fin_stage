from tkinter import *
import tkcalendar as tk
from tkinter.font import Font
from tkinter import messagebox as mb

class add_event:
    def __init__(self, root, width, height):
        self.fonts = ('Arial', 14, 'bold')
        self.page = Canvas(root, width=width, height=height, bg="#333333")
        self.font = Font(family="Helvetica", size=12, underline=True, slant="italic", weight="bold")
        Label(self.page, text="1.       Enregitrement de vos rendez vous.", font=self.font, bg="#333333",
              fg="pink").place(x=20, y=20)
        Label(self.page, text="Entrer les informations du nouveau rendez-vous. ", font=self.fonts, bg="#333333",
              fg="pink").place(x=130, y=80)
        Label(self.page, text="vous aurez rendez-vous avec : Mr / Mme ", font=self.fonts, bg="#333333", fg="pink").place(x=175, y=150)
        self.nom=Entry(self.page, font=self.fonts)
        self.nom.place(x=560, y=150, width=200)
        Label(self.page, text="Sexe: ", font=self.fonts, bg="#333333", fg="pink").place(x=175, y=180)
        i = IntVar()
        Radiobutton(self.page, text=" Homme ", value=1, variable=i, bg="#333333", activebackground="#333333",
                    activeforeground="black").place(x=270, y=180)
        Radiobutton(self.page, text="Femme", value=2, variable=i, bg="#333333", activebackground="#333333",
                    activeforeground="black").place(x=400, y=180)

        Label(self.page, text="Lieu du rendez-vous : ", font=self.fonts, bg="#333333", fg="pink").place(x=175, y=215)
        self.lieu=Entry(self.page, font=self.fonts)
        self.lieu.place(x=420, y=215,width=200)
        Label(self.page, text="STATUS : ", fg="pink", font=("Arial", 14, "bold"), bg="#333333").place(x=175, y=245)
        j = IntVar()
        Radiobutton(self.page, text="Traité", value=1, variable=j, bg="#333333", font=("Arial", 12, "italic"),
                    activebackground="#333333").place(x=270, y=245)
        Radiobutton(self.page, text="Non Traité", value=2, variable=j, bg="#333333", font=("Arial", 12, "italic"),
                    activebackground="#333333").place(x=350, y=245)
        Label(self.page, text="Date du rendez-vous: ", font=self.fonts, bg="#333333", fg="pink").place(x=175, y=295)
        self.date=tk.DateEntry(self.page)
        self.date.place(x=420, y=295,width=160)
        Label(self.page, text="Heure du rendez-vous : ", font=self.fonts, bg="#333333", fg="pink").place(x=175, y=340)
        Spinbox(self.page,from_=00, to=24, width=3).place(x=420, y=345)
        Label(self.page,text="H",bg="#333333",fg="pink",width=1).place(x=450,y=345)
        Spinbox(self.page, from_=00, to=60, width=3).place(x=465, y=345)
        Label(self.page, text="Mins",width=3,bg="#333333",fg="pink").place(x=500,y=345)
        Label(self.page, text="Motif du rendez-vous : ", font=self.fonts, bg="#333333", fg="pink").place(x=175, y=380)
        self.motif=Entry(self.page, font=self.fonts)
        self.motif.place(x=420, y=380, width=200)
        Label(self.page, text="Contact: ", font=self.fonts, bg="#333333", fg="pink").place(x=175, y=420)
        self.contact=Entry(self.page, font=self.fonts)
        self.contact.place(x=420, y=420, width=200)
        Button(self.page, text="  Enregistrer  ", font=self.fonts, bg="blue", fg="white",activebackground="#333333"
               ,command=self.enregistre).place(x=220, y=490)
        Button(self.page, text="    Effacer    ", font=("arial", 14, "italic"), bg="orange", fg="white",
               activebackground="#333333", activeforeground="white", command=self.supprimer).place(x=390, y=490)

        Label(self.page, text="Pour modifier le status d'une factutre pré-enregistrez, cliquez ici : "
              , fg="white", font=("Arial", 9, "bold"), bg="yellow").place(x=width- 200, y=height - 100)

        Button(self.page, text="  Modif.stat  ", font=("arial", 9, "italic"), bg="blue", fg="white",
               activebackground="yellow", activeforeground="red").place(x=width / 2 + 70, y=height - 100)

        # Button(
        #   self.page, text="Go to home",
        #  command=lambda :HomePage(self.page, width=800, height=500),font=self.fonts, bg="#333333",fg="cadetblue1").place(x=510, y=320)
        self.page.place(x=200, y=51)

    def enregistre(self):
        mb.askyesno("confirmer", "vous confirmer que les informations entrez sont correctes? ")

    def supprimer(self):
        test=mb.askyesno("confirmer", "Voulez- vous vraiment vider tous les champs ? ")
        if test:
            self.motif.delete(0,END)
            self.nom.delete(0,END)
            self.lieu.delete(0,END)
            self.contact.delete(0,END)
            self.date.delete(0,END) 