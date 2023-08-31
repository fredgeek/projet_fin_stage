from tkinter import *
from tkinter.font import Font


class mon_compte:

    def __init__(self, root, width,height,nom,tel,email,password):

        self.width=width
        self.height=height
        self.fonts=Font(family="Helvetica",size=13,underline=True,slant="italic",weight="bold")
        self.page=Canvas(root,width=self.width,height=self.height,bg="#7fc3c0")

        Label(self.page, text="consulter vos informations personelles: ",font=self.fonts
              ,bg="#7fc3c0" ,fg="white").place(x=self.width/4,y=60)

        Label(self.page,text="Votre NOM : ",font=self.fonts,bg="#7fc3c0").place(x=50,y=200)
        name=nom
        Label(self.page,str(name) ,font=("arial",12,"roman"),bg="#7fc3c0").place(x=250,y=200)
        
        num_tel=tel
        Label(self.page,text="Votre TEL : ",font=self.fonts,bg="#7fc3c0").place(x=50,y=280)
        Label(self.page,str(num_tel) ,font=("arial",12,"roman"),bg="#7fc3c0").place(x=250,y=280)
        
        Label(self.page, text="Votre Email : ",font=self.fonts,bg="#7fc3c0").place(x=50, y=350)
        Email = email
        Label(self.page, str(Email),font=("arial",12,"roman"),bg="#7fc3c0").place(x=250, y=350)

        Label(self.page, text="Votre Mot de passe : ",font=self.fonts,bg="#7fc3c0").place(x=50, y=430)
        pass_word = password
        Label(self.page, str(pass_word),font=("arial",12,"roman"),bg="#7fc3c0").place(x=250, y=430)




        self.page.place(x=200,y=51)