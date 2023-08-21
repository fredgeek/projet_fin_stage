# importation des dependances ...
from tkinter import *

from pages.authentication.login_page import LoginPage


class MainApp:
    def __init__(self):
        self.root = Tk()

        self.root.geometry("800x500")

        # premiere page ....
        LoginPage(self.root,width=800,height=500)


        # adffichage de la fenetre
        self.root.mainloop()

ma_fenetre = MainApp()

print(ma_fenetre)




