from tkinter import *


class delete_clients:
    def __init__(self, root, width, height):
        self.fonts = ('Arial', 14, 'bold')
        self.page = Canvas(root, width=width, height=height, bg="#333333")
        Label(self.page, text="Quels Clients voulez-vous supprimer?   . ", font=self.fonts, bg="#333333",
              fg="pink").place(x=130, y=80)
        Label(self.page, text="NOM : ", font=self.fonts, bg="#333333", fg="pink").place(x=200, y=150)
        Entry(self.page, font=self.fonts).place(x=360, y=150)
        Label(self.page, text="Email  ", font=self.fonts, bg="#333333", fg="pink").place(x=200, y=210)
        Entry(self.page, font=self.fonts).place(x=360, y=210)
        Button(self.page, text="Supprimer", font=self.fonts, bg="#333333", fg="cadetblue1").place(x=215, y=320)

        # Button(
        #   self.page, text="Go to home",
        #  command=lambda :HomePage(self.page, width=800, height=500),font=self.fonts, bg="#333333",fg="cadetblue1").place(x=510, y=320)
        self.page.place(x=150, y=51)