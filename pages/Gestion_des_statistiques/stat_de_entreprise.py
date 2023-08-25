from tkinter import *
from tkinter import ttk

class Nbr_clients:
    def __init__(self, root, width, height):
        self.fonts = ('Arial', 14, 'bold')
        self.width=width
        self.height=height
        ################# creation du canvas d'affichage ##################

        self.page = Canvas(root, width=self.width, height=self.height, bg="violet")
        # affichage du nombre d'employer
       
        


        self.page.place(x=200, y=51)