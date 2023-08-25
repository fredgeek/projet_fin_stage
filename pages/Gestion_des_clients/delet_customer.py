from tkinter import *


class delete_clients:
    def __init__(self, root, width, height):
        self.fonts = ('Arial', 14, 'bold')
        self.page = Canvas(root, width=width, height=height, bg="#1c141f")
        Label(self.page, text="supprimer un  client ", font=self.fonts, bg="#1c141f",
              fg="pink").place(x=95, y=50)
        Label(self.page, text="Quel client voulez vous supprimer ? ", font=self.fonts, bg="#1c141f",
              fg="pink").place(x=180, y=120)
        Label(self.page, text="NOM : ", font=self.fonts,bg="#1c141f", fg="pink").place(x=130, y=200)
        Entry(self.page, font=self.fonts).place(x=200, y=200)
        Label(self.page, text="Email : ", font=self.fonts,bg="#1c141f", fg="pink").place(x=450, y=200)
        Entry(self.page, font=self.fonts).place(x=520, y=200)
        Label(self.page, text="Tel : ", font=self.fonts,bg="#1c141f", fg="pink").place(x=130, y=260)
        Entry(self.page, font=self.fonts).place(x=200, y=260)

        Button(self.page, text="Supprimer", font=self.fonts,bg="#1c141f", fg="cadetblue1", bd=0).place(x=215, y=320)
        Button(self.page, text="Tous effacer", font=self.fonts,bg="#1c141f", fg="cadetblue1",bd=0).place(x=250, y=320)


        # Button(
        #   self.page, text="Go to home",
        #  command=lambda :HomePage(self.page, width=800, height=500),font=self.fonts, bg="#333333",fg="cadetblue1").place(x=510, y=320)
        self.page.place(x=200, y=51)