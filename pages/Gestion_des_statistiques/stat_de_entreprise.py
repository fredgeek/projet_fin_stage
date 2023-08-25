from tkinter import *
from tkinter import ttk

class Nbr_clients:
    def __init__(self, root, width, height):
        self.fonts = ('Arial', 14, 'bold')
        self.width=width
        self.height=height
        
        
        ################# creation du canvas d'affichage ##################
        self.page = Canvas(root, width=self.width, height=self.height, bg="violet")
        
        Label(self.page,text="Les statistiques de l'entreprise.",bg="violet",font=self.fonts).place(x=95, y=50)
        # affichage du nombre d'employer
        self.stat_activite=Canvas(self.page,width=230,height=150,bg="white")
        Label(self.page,text="Activités",bg="violet",font=self.fonts ).place(x=93,y=102)
        nbr_activite= "--"
        Label(self.stat_activite,fg="black",font=self.fonts ,bg="white",text="Vous avez deja efectuer ").place(x=20,y=20)
        Label(self.stat_activite,fg="black",font=self.fonts ,bg="white",text=""+nbr_activite).place(x=20,y=40)
        Label(self.stat_activite,fg="black",font=self.fonts ,bg="white",text="rendez-vous").place(x=32,y=60)
        self.stat_activite.place(x=90,y=130)


        
        
        
        self.stat_client=Canvas(self.page,width=230,height=150,bg="white").place(x=510,y=130)
        Label(self.page,text="clients",bg="violet",font=self.fonts ).place(x=513,y=102)
        nbr_client="--"
        Label(self.stat_client,fg="black",font=self.fonts,bg="white",text="Vous avez deja ").place(x=745,y=200)
        Label(self.stat_client,fg="black",font=self.fonts,bg="white",text=""+nbr_client).place(x=800,y=250)
        Label(self.stat_client,fg="black",font=self.fonts,bg="white",text="clients").place(x=780,y=290)


        
        
        self.stat_employe=Canvas(self.page,width=230,height=150,bg="white").place(x=90,y=360)
        Label(self.page,text="Employés",bg="violet",font=self.fonts ).place(x=83,y=332)
        nbr_employe="--"
        Label(self.stat_employe,fg="black",font=self.fonts,bg="white",text="Vous avez deja ").place(x=312,y=420)
        Label(self.stat_employe,fg="black",font=self.fonts,bg="white",text=""+nbr_employe).place(x=385,y=470)
        Label(self.stat_employe,fg="black",font=self.fonts,bg="white",text="employés").place(x=340,y=505)



        
        
        self.stat_finance=Canvas(self.page,width=230,height=150,bg="white",).place(x=510,y=360)
        Label(self.page,text="Finances",bg="violet",font=self.fonts ).place(x=513,y=332)
        nbr_operation="--"
        Label(self.stat_client,fg="black",bg="white",text="-Vous avez deja "+nbr_operation+"clients").place(x=720,y=420)

    
        
        self.page.place(x=200, y=51)