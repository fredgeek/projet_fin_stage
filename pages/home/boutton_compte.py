from tkinter import *
from tkinter.font import Font


class mon_compte:

    def __init__(self, root, width, height):

        self.width=width
        self.height=height
        self.fonts=Font(family="Helvetica",size=13,underline=True,slant="italic",weight="bold")
        self.page=Canvas(root,width=self.width,height=self.height,bg="#555555")

        Label(self.page, text="consulter vos informations personelles: ",font=self.fonts
              ,bg="#555555").place(x=self.width/4,y=4)

        Label(self.page,text="NOM et PRENOM : ",font=self.fonts,bg="#555555").place(x=50,y=200)
        nom=" username_nom"
        prenom=" username_prenom"
        Label(self.page,text=f"{nom} {prenom}" ,font=("arial",12,"roman"),bg="#555555").place(x=250,y=200)

        Label(self.page, text="Email : ",font=self.fonts,bg="#555555").place(x=50, y=300)
        email = " username_email"
        Label(self.page, text=f"{email} ",font=("arial",12,"roman"),bg="#555555").place(x=250, y=300)

        Label(self.page, text="Mot de passe : ",font=self.fonts,bg="#555555").place(x=50, y=400)
        password = " username_password"
        Label(self.page, text=f"{password} ",font=("arial",12,"roman"),bg="#555555").place(x=250, y=400)




        self.page.place(x=200,y=51)