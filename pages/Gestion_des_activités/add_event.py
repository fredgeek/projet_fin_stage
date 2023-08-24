from tkinter import *
import tkcalendar as tk


class add_event:
    def __init__(self, root, width, height):
        self.fonts = ('Arial', 14, 'bold')
        self.page = Canvas(root, width=width, height=height, bg="#333333")
        Label(self.page, text="Entrer les informations du nouveau rendez-vous. ", font=self.fonts, bg="#333333",
              fg="pink").place(x=130, y=80)
        Label(self.page, text="Lieu du rendez-vous : ", font=self.fonts, bg="#333333", fg="pink").place(x=175, y=150)
        Entry(self.page, font=self.fonts).place(x=395, y=150)
        Label(self.page, text="Date du rendez-vous: ", font=self.fonts, bg="#333333", fg="pink").place(x=175, y=210)
        self.date=tk.DateEntry(self.page).place(x=395, y=210)
        Label(self.page, text="A quel heur est le rende : ", font=self.fonts, bg="#333333", fg="pink").place(x=175, y=270)
        Entry(self.page, font=self.fonts).place(x=420, y=270)
        Button(self.page, text="Enregistrer", font=self.fonts, bg="#333333", fg="cadetblue1").place(x=215, y=400)

        # Button(
        #   self.page, text="Go to home",
        #  command=lambda :HomePage(self.page, width=800, height=500),font=self.fonts, bg="#333333",fg="cadetblue1").place(x=510, y=320)
        self.page.place(x=150, y=51)