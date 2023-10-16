class Animal:
    def __init__(self, nom, espece):
        self.nom = nom
        self.espece = espece

    def faire_son_cri(self):
        pass  # Cette méthode sera redéfinie dans les sous-classes

class Chien(Animal):
    def faire_son_cri(self):
        return "Woof!"

class Chat(Animal):
    def faire_son_cri(self):
        return "Meow!"

# Utilisation des classes
mon_chien = Chien("Fido", "Chien")
mon_chat = Chat("Whiskers", "Chat")

print(mon_chien.nom, mon_chien.faire_son_cri())  # Affiche : "Fido Woof!"
print(mon_chat.nom, mon_chat.faire_son_cri())  # Affiche : "Whiskers Meow!"
