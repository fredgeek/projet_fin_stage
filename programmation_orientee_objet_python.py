class Toto:
    pass
class Ordinateur:
    couleur = 'rouge'

    # constructeur de la classe
    def __init__(self,name,core,clavier):
        # attributs de la classe.
        self.core = core
        self.clavier = clavier
        self.name = name

    # methodes de la classe ....
    def allumer(self):
        return f'{self.name} est allume !!! '
    def eteindre(self):
        return f'{self.name} est eteint !!! '



ordi1 = Ordinateur('HP',5,'anglais')
print('ordi 1: ',ordi1.core)
print(ordi1.allumer())

ordi2 = Ordinateur('MacBook',7,'francais')
print('ordi 2: ',ordi2.core)
print(ordi2.allumer())


