from tkinter import*

# création de l'interface de la page d'accueil
interface1 = Tk()
interface1.iconbitmap("téléchargement-_8_.ico")
interface1.geometry("700x500")
interface1.config(background = 'green')
interface1.title("Page d'accueil")

#demande a l utilisateur d'entrer ces informations.

nom = Label(interface1, text="Entrer votre nom", fg="red")
nom.pack()
prenom = Label(interface1, text="Entrer votre prenom",fg="red")
prenom.pack()
age = Label(interface1, text="Entrez votre age",fg="red").pack()

email = Label(interface1, text="Entrez votre email",fg="red").pack()

date_naiss = Label(interface1, text="Entrez votre date de naissance",fg="red")


Label(inter)




interface1.mainloop()