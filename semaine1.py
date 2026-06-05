# Variables et types
nom = "Agent IA"
version = 1.0
actif = True

print(f"Nom : {nom}, Version : {version}, Actif : {actif}")

# Fonction simple
def saluer(prenom):
    return f"Bonjour {prenom}, bienvenue dans la formation !"

print(saluer("Maho"))

# Boucle
langages = ["Python", "LangChain", "ChromaDB", "Streamlit"]
for langage in langages:
    print(f"→ {langage}")