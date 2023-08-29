from tkinter import *
from tkinter import ttk

class Nbr_clients:
    def __init__(self, root, width, height):
        self.fonts = ('Arial', 14, 'bold')
        self.width=width
        self.height=height
        
        
        ################# creation du canvas d'affichage ##################
        self.page = Canvas(root, width=self.width, height=self.height, bg="#1c141f")
        
        Label(self.page,text="Les statistiques de l'entreprise.",bg="#1c141f",fg="pink",font=self.fonts).place(x=95, y=50)
        # affichage du nombre d'employer
        self.stat_activite=Canvas(self.page,width=230,height=150,bg="white")
        Label(self.page,text="Activités",bg="#1c141f",fg="pink",font=self.fonts ).place(x=93,y=102)
        nbr_activite= "--"
        Label(self.stat_activite,fg="black",font=self.fonts ,bg="white",text="Vous avez deja efectué ").place(x=6,y=20)
        Label(self.stat_activite,fg="black",font=self.fonts ,bg="white",text=""+nbr_activite).place(x=95,y=65)
        Label(self.stat_activite,fg="black",font=self.fonts ,bg="white",text="rendez-vous").place(x=45,y=105)
        self.stat_activite.place(x=90,y=130)


        
        
        
        self.stat_client=Canvas(self.page,width=230,height=150,bg="white")
        Label(self.page,text="clients",bg="#1c141f",fg="pink",font=self.fonts ).place(x=513,y=102)
        nbr_client="--"
        Label(self.stat_client,fg="black",font=self.fonts,bg="white",text="Vous avez deja ").place(x=35,y=20)
        Label(self.stat_client,fg="black",font=self.fonts,bg="white",text=""+nbr_client).place(x=95,y=65)
        Label(self.stat_client,fg="black",font=self.fonts,bg="white",text="clients").place(x=70,y=105)
        self.stat_client.place(x=510,y=130)


        
        
        self.stat_employe=Canvas(self.page,width=230,height=150,bg="white")
        Label(self.page,text="Employés",bg="#1c141f",fg="pink",font=self.fonts ).place(x=83,y=332)
        nbr_employe="--"
        Label(self.stat_employe,fg="black",font=self.fonts,bg="white",text="Vous avez deja ").place(x=35,y=20)
        Label(self.stat_employe,fg="black",font=self.fonts,bg="white",text=""+nbr_employe).place(x=95,y=65)
        Label(self.stat_employe,fg="black",font=self.fonts,bg="white",text="employés").place(x=65,y=105)
        self.stat_employe.place(x=90,y=360)



        
        
        self.stat_finance=Canvas(self.page,width=230,height=150,bg="white",)
        Label(self.page,text="Finances",bg="#1c141f",fg="pink",font=self.fonts ).place(x=513,y=332)
        nbr_operation="--"
        Label(self.stat_finance,fg="black",font=self.fonts,bg="white",text="Vous avez deja effectué ").place(x=6,y=20)
        Label(self.stat_finance,fg="black",font=self.fonts,bg="white",text=""+nbr_operation).place(x=95,y=65)
        Label(self.stat_finance,fg="black",font=self.fonts,bg="white",text="operations").place(x=45,y=105)
        self.stat_finance.place(x=510,y=360) 

    
        
        self.page.place(x=200, y=51)