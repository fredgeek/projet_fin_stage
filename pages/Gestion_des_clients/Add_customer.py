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
        self.nom=Entry(self.page, font=self.fonts)
        self.nom.place(x=380, y=120)
        Label(self.page, text="Email : ", font=self.fonts, bg="#333333", fg="pink").place(x=200, y=180)
        self.email=Entry(self.page, font=self.fonts)
        self.email.place(x=380, y=180)
        Label(self.page, text="TEL : ", font=self.fonts, bg="#333333", fg="pink").place(x=200, y=312)
        self.tel=Entry(self.page, font=self.fonts)
        self.tel.place(x=380, y=312)
        Label(self.page, text="Sexe : ", font=self.fonts, bg="#333333", fg="pink").place(x=200, y=230)
        i = IntVar()
        Radiobutton(self.page, text=" Homme ", value=1, variable=i, bg="#333333", activebackground="#333333",
                    activeforeground="black").place(x=380, y=230)
        Radiobutton(self.page, text="Femme", value=2, variable=i, bg="#333333", activebackground="#333333",
                    activeforeground="black").place(x=470, y=230)
        Button(self.page, text="Enregistrer", font=self.fonts, bg="blue", fg="cadetblue1"
               , activebackground="#333333", activeforeground="blue", command=self.enregistre).place(x=215, y=450)
        Button(self.page, text="Vider les champs ", font=self.fonts, bg="orange", fg="cadetblue1"
               , activebackground="#333333", activeforeground="red", command=self.supprimer).place(x=415, y=450)

        Label(self.page, text="Quartier: ", font=self.fonts, bg="#333333", fg="pink").place(x=200, y=270)
        self.quat=Entry(self.page, font=self.fonts)
        self.quat.place(x=380, y=270)
        Label(self.page, text="Ville: ", font=self.fonts, bg="#333333", fg="pink").place(x=200, y=360)
        self.ville=Entry(self.page, font=self.fonts)
        self.ville.place(x=380, y=360)
        Label(self.page, text="Secteur d'activité: ", font=self.fonts, bg="#333333", fg="pink").place(x=200, y=395)
        self.sect_acti=Entry(self.page, font=self.fonts)
        self.sect_acti.place(x=380, y=395)
        # Button(
        #   self.page, text="Go to home",
        #  command=lambda :HomePage(self.page, width=800, height=500),font=self.fonts, bg="#333333",fg="cadetblue1").place(x=510, y=320)
        self.page.place(x=200, y=51)

    def enregistre(self):
        mb.askyesno("confirmer", "vous confirmer que les informations entrez sont correctes? ")

    def supprimer(self):
        test=mb.askyesno("confirmer", "Voulez- vous vraiment vider tous les champs ? ")
        if test:
            self.quat.delete(0,END)
            self.sect_acti.delete(0,END)
            self.tel.delete(0,END)
            self.email.delete(0,END)
            self.nom.delete(0,END)
            self.ville.delete(0,END)