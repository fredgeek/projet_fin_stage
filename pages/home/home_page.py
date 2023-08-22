from tkinter import *

class HomePage:
    def __init__(self,root,width,height):
        # dimensions de la fenetre
        self.width = width
        self.height = height

        # root = fenetre parent, width et height sont les dimensions de la fenetre
        self.page = Canvas(root,width=self.width,height=self.height,bg="yellow")
        Label(self.page,text="Home page").place(x=40,y=20)

        #bouton de transition ver le register_page
        Button(
            self.page, text="Back button ",
               command=self.page.destroy).place(x=90,y=60)


        self.page.place(x=0,y=0)


