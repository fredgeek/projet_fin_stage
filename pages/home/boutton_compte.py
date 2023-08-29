from tkinter import *
from tkinter.font import Font


class mon_compte:

    def __init__(self, root, width, height):

        self.width=width
        self.height=height
        self.fonts=Font(family="Helvetica",size=13,underline=True,slant="italic",weight="bold")
        self.page=Canvas(root,width=self.width,height=self.height,bg="#7fc3c0")

        Label(self.page, text="consulter vos informations personelles: ",font=self.fonts
              ,bg="#7fc3c0" ,fg="white").place(x=self.width/4,y=60)

        Label(self.page,text="NOM et PRENOM : ",font=self.fonts,bg="#7fc3c0").place(x=50,y=200)
        nom=" username_nom"
        prenom=" username_prenom"
        Label(self.page,text=f"{nom} {prenom}" ,font=("arial",12,"roman"),bg="#7fc3c0").place(x=250,y=200)
        tel="num_tel"
        Label(self.page,text="TEL : ",font=self.fonts,bg="#7fc3c0").place(x=50,y=280)
        Label(self.page,text=f" {tel}" ,font=("arial",12,"roman"),bg="#7fc3c0").place(x=250,y=280)

        Label(self.page, text="Email : ",font=self.fonts,bg="#7fc3c0").place(x=50, y=350)
        email = " username_email"
        Label(self.page, text=f"{email} ",font=("arial",12,"roman"),bg="#7fc3c0").place(x=250, y=350)

        Label(self.page, text="Mot de passe : ",font=self.fonts,bg="#7fc3c0").place(x=50, y=430)
        password = " username_password"
        Label(self.page, text=f"{password} ",font=("arial",12,"roman"),bg="#7fc3c0").place(x=250, y=430)




        self.page.place(x=200,y=51)