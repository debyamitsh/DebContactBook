class Contact:
    def __init__(self):
        self.info = {}  # Dictionnaire pour stocker les contacts

    def afficher(self):
        """ Affiche tous les contacts enregistrés """
        if not self.info:
            print("Aucun contact enregistré.")
        else:
            for key, value in self.info.items():
                print(f"{key} : {value}")

    def ajouter(self, nom, numero):
        """ Ajoute un contact """
        self.info[nom] = numero
        return f"Numéro de {nom} enregistré avec succès."

    def rechercher(self, nom):
        """ Recherche un contact """
        return self.info.get(nom, "Contact non trouvé")

    def supprimer(self, nom):
        """ Supprime un contact """
        if nom in self.info:
            del self.info[nom]
            return f"Contact {nom} supprimé."
        return "Contact non trouvé."

# Instanciation de l'objet Contact
contacts = Contact()

while True:
    print("\n1. Ajouter un contact")
    print("2. Rechercher un contact")
    print("3. Supprimer un contact")
    print("4. Afficher les contacts")
    print("5. Quitter")

    choix = input("Choisissez une option : ")

    if choix == "1":
        nom = input("Entrez le nom : ")
        numero = input("Entrez le numéro : ")
        print(contacts.ajouter(nom, numero))

    elif choix == "2":
        nom = input("Entrez le nom à rechercher : ")
        print(f"Numéro : {contacts.rechercher(nom)}")

    elif choix == "3":
        nom = input("Entrez le nom à supprimer : ")
        print(contacts.supprimer(nom))

    elif choix == "4":
        contacts.afficher()

    elif choix == "5":
        print("Au revoir !")
        break

    else:
        print("Choix invalide. Veuillez réessayer.")