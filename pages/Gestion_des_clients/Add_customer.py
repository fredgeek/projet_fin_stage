from tkinter import *
from tkinter import messagebox as mb
from tkinter.font import Font


class ajout_clients:
    def __init__(self, root, width, height):
        self.fonts = ('Arial', 14, 'bold')
        self.page = Canvas(root, width=width, height=height, bg="#333333")
        self.font = Font(family="Helvetica", size=12, underline=True, slant="italic", weight="bold")
        Label(self.page, text="1.     Ajouter un nouveau client ", font=self.font, bg="#333333", fg="pink").place(
            x=20, y=20)

        Label(self.page, text="Entrer les informations du clients  a enregistrer . "
              , font=self.fonts, bg="#333333", fg="pink").place(x=130, y=80)
        Label(self.page, text="NOM : ", font=self.fonts, bg="#333333", fg="pink").place(x=200, y=120)
        Entry(self.page, font=self.fonts).place(x=280, y=120)
        Label(self.page, text="Email : ", font=self.fonts, bg="#333333", fg="pink").place(x=200, y=180)
        Entry(self.page, font=self.fonts).place(x=280, y=180)
        Label(self.page, text="TEL : ", font=self.fonts, bg="#333333", fg="pink").place(x=200, y=312)
        Entry(self.page, font=self.fonts).place(x=280, y=312)
        Label(self.page, text="Sexe : ", font=self.fonts, bg="#333333", fg="pink").place(x=200, y=230)
        i = IntVar()
        Radiobutton(self.page, text=" Homme ", value=1, variable=i, bg="#333333", activebackground="#333333",
                    activeforeground="black").place(x=270, y=230)
        Radiobutton(self.page, text="Femme", value=2, variable=i, bg="#333333", activebackground="#333333",
                    activeforeground="black").place(x=400, y=230)
        Button(self.page, text="Enregistrer", font=self.fonts, bg="#333333", fg="cadetblue1"
               , activebackground="#333333", activeforeground="blue", command=self.enregistre).place(x=215, y=450)
        Button(self.page, text="Vider les champs ", font=self.fonts, bg="#333333", fg="cadetblue1"
               , activebackground="#333333", activeforeground="red", command=self.supprimer).place(x=415, y=450)

        Label(self.page, text="Quartier: ", font=self.fonts, bg="#333333", fg="pink").place(x=200, y=270)
        Entry(self.page, font=self.fonts).place(x=300, y=270)
        Label(self.page, text="Ville: ", font=self.fonts, bg="#333333", fg="pink").place(x=200, y=360)
        Entry(self.page, font=self.fonts).place(x=280, y=360)
        Label(self.page, text="Secteur d'activité: ", font=self.fonts, bg="#333333", fg="pink").place(x=200, y=395)
        Entry(self.page, font=self.fonts).place(x=380, y=395)
        # Button(
        #   self.page, text="Go to home",
        #  command=lambda :HomePage(self.page, width=800, height=500),font=self.fonts, bg="#333333",fg="cadetblue1").place(x=510, y=320)
        self.page.place(x=200, y=51)

    def enregistre(self):
        mb.askyesno("confirmer", "vous confirmer que les informations entrez sont correctes? ")

    def supprimer(self):
        mb.askyesno("confirmer", "Voulez- vous vraiment vider tous les champs ? ")