# importation des dependances ...
from tkinter import *

from pages.authentication.login_page import LoginPage


class MainApp:
    def __init__(self):
        self.root = Tk()
        self.root.title("PersonalsManager")
        self.root.geometry("800x500")
        self.root.iconbitmap("icone.ico")
        #self.root.resizable(width=False,height=False)
        # premiere page ....
        self.first_window = LoginPage(self.root,width=800,height=500)


        # adffichage de la fenetre
        self.root.mainloop()

ma_fenetre = MainApp()

print(ma_fenetre)




