nom = "Odilon"
age = 25
competences = ["Python","Langchain"]
def presenter(prenom):
    return f"Bonjour, je m'appelle {nom}, j'ai {age} ans. Je vais apprendre 5 compétences"
print(presenter("Maho"))
# Boucle
langages = ["Python", "LangChain", "ChromaDB", "Streamlit"]
for langage in langages:
    print(f"→ {langage}")