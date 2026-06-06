#Dictionnaires
personne = {
    "prenom": "Maho",
    "age": 25,
    "ville": "Cotonou"
}
print(personne["prenom"])   # → Maho
print(personne["ville"])    # → Cotonou
personne["metier"] = "Développeur IA"
print(personne["metier"])   # → Développeur IA
# Afficher toutes les clés et valeurs
for cle, valeur in personne.items():
    print(f"{cle} : {valeur}")
# Les Classes
class Agent:
    def __init__(self, nom, specialite):
        self.nom = nom
        self.specialite = specialite
    
    def se_presenter(self):
        return f"Je suis {self.nom}, spécialisé en {self.specialite}"

# Créer un agent
agent1 = Agent("Maho", "Intelligence Artificielle")
print(agent1.se_presenter())

import csv

# Écrire un fichier CSV
with open("agents.csv", "w", newline="") as fichier:
    writer = csv.writer(fichier)
    writer.writerow(["nom", "specialite", "ville"])
    writer.writerow(["Maho", "Intelligence Artificielle", "Cotonou"])
    writer.writerow(["Alice", "LangChain", "Paris"])
    writer.writerow(["Bob", "ChromaDB", "Lyon"])

print("Fichier CSV créé !")

# Lire le fichier CSV
with open("agents.csv", "r") as fichier:
    reader = csv.reader(fichier)
    for ligne in reader:
        print(ligne)