from tkinter import *


class ajout_clients:
    def __init__(self, root, width, height):
        self.fonts = ('Arial', 14, 'bold')
        self.page = Canvas(root, width=width, height=height,bg="#1c141f")
        Label(self.page, text="Ajouter un nouveau client ", font=self.fonts, bg="#1c141f",
              fg="pink").place(x=95, y=50)
        Label(self.page, text="Entrer les informations du clients  . ", font=self.fonts, bg="#1c141f",
              fg="pink").place(x=180, y=120)
        Label(self.page, text="NOM : ", font=self.fonts,bg="#1c141f", fg="pink").place(x=130, y=200)
        Entry(self.page, font=self.fonts).place(x=200, y=200)
        Label(self.page, text="Sex : ", font=self.fonts,bg="#1c141f", fg="pink").place(x=440, y=200)
        Entry(self.page, font=self.fonts).place(x=500, y=200)
        Label(self.page, text="Email : ", font=self.fonts,bg="#1c141f", fg="pink").place(x=130, y=250)
        Entry(self.page, font=self.fonts).place(x=200, y=250)
        Label(self.page, text="Tel : ", font=self.fonts,bg="#1c141f", fg="pink").place(x=440, y=250)
        Entry(self.page, font=self.fonts).place(x=500, y=250)
        Label(self.page, text="Quartier : ", font=self.fonts,bg="#1c141f", fg="pink").place(x=100, y=300)
        Entry(self.page, font=self.fonts).place(x=200, y=300)
        Label(self.page, text="Ville : ", font=self.fonts,bg="#1c141f", fg="pink").place(x=440, y=300)
        Entry(self.page, font=self.fonts).place(x=500, y=300)
        Label(self.page, text="Secteur D'activité : ", font=self.fonts,bg="#1c141f", fg="pink").place(x=130, y=350)
        Entry(self.page, font=self.fonts).place(x=320, y=350)
        Button(self.page, text="Ajouter", font=self.fonts,bg="#1c141f", fg="cadetblue1",bd=0).place(x=230, y=380)

        # Button(
        #   self.page, text="Go to home",
        #  command=lambda :HomePage(self.page, width=800, height=500),font=self.fonts, bg="#333333",fg="cadetblue1").place(x=510, y=320)
        self.page.place(x=150, y=51)