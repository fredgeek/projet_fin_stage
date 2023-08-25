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
        Entry(self.page, font=self.fonts).place(x=560, y=150, width=200)
        Label(self.page, text="Sexe: ", font=self.fonts, bg="#333333", fg="pink").place(x=175, y=180)
        i = IntVar()
        Radiobutton(self.page, text=" Homme ", value=1, variable=i, bg="#333333", activebackground="#333333",
                    activeforeground="black").place(x=270, y=180)
        Radiobutton(self.page, text="Femme", value=2, variable=i, bg="#333333", activebackground="#333333",
                    activeforeground="black").place(x=400, y=180)

        Label(self.page, text="Lieu du rendez-vous : ", font=self.fonts, bg="#333333", fg="pink").place(x=175, y=215)
        Entry(self.page, font=self.fonts).place(x=420, y=215,width=200)
        Label(self.page, text="Date du rendez-vous: ", font=self.fonts, bg="#333333", fg="pink").place(x=175, y=280)
        self.date=tk.DateEntry(self.page).place(x=420, y=280,width=160)
        Label(self.page, text="Heure du rendez-vous : ", font=self.fonts, bg="#333333", fg="pink").place(x=175, y=340)
        Spinbox(self.page,from_=00, to=24, width=3).place(x=420, y=345)
        Label(self.page,text="H",bg="#333333",fg="pink",width=1).place(x=450,y=345)
        Spinbox(self.page, from_=00, to=60, width=3).place(x=465, y=345)
        Label(self.page, text="Mins",width=3,bg="#333333",fg="pink").place(x=500,y=345)
        Label(self.page, text="Motif du rendez-vous : ", font=self.fonts, bg="#333333", fg="pink").place(x=175, y=370)
        Entry(self.page, font=self.fonts).place(x=420, y=370, width=200)
        Label(self.page, text="Contact: ", font=self.fonts, bg="#333333", fg="pink").place(x=175, y=410)
        Entry(self.page, font=self.fonts).place(x=420, y=410, width=200)
        Button(self.page, text="Enregistrer", font=self.fonts, bg="#333333", fg="cadetblue1",activebackground="#333333"
               ,command=self.enregistre).place(x=315, y=500)
        Button(self.page, text="Liberez les champs ", font=("arial", 14, "italic"), bg="#333333", fg="green",
               activebackground="#333333", activeforeground="red", command=self.supprimer).place(x=505, y=500)

        # Button(
        #   self.page, text="Go to home",
        #  command=lambda :HomePage(self.page, width=800, height=500),font=self.fonts, bg="#333333",fg="cadetblue1").place(x=510, y=320)
        self.page.place(x=200, y=51)

    def enregistre(self):
        mb.askyesno("confirmer", "vous confirmer que les informations entrez sont correctes? ")

    def supprimer(self):
        mb.askyesno("confirmer", "Voulez- vous vraiment vider tous les champs ? ")