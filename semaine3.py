import os
# os est un module Python qui permet d'accéder au système
# on l'utilise pour lire les variables d'environnement

from openai import OpenAI
# on importe la classe OpenAI depuis le package openai
# c'est cette classe qui nous permet de parler à l'API

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
# on crée une connexion avec l'API OpenAI
# os.environ.get("OPENAI_API_KEY") lit la clé API
# qu'on a sauvegardée dans ~/.bashrc tout à l'heure

def generer_contenu(sujet, style):
# on définit une fonction qui prend 2 paramètres :
# sujet = le thème à expliquer
# style = le style d'écriture choisi

    styles = {
    # on crée un dictionnaire avec 3 styles différents
    # chaque clé est un nom de style
    # chaque valeur est une instruction pour le modèle IA

        "formel": "Tu es un expert professionnel. Explique de façon formelle et académique.",
        # style formel : langage professionnel et académique

        "vulgarise": "Tu es un vulgarisateur. Explique simplement comme à un enfant de 12 ans.",
        # style vulgarisé : langage simple et accessible

        "technique": "Tu es un ingénieur expert. Explique de façon très technique et précise."
        # style technique : langage précis pour les experts
    }

    response = client.chat.completions.create(
    # on envoie une requête à l'API OpenAI
    # client.chat.completions.create() = la fonction principale pour parler au modèle

        model="gpt-3.5-turbo",
        # on choisit le modèle GPT-3.5 Turbo
        # c'est le moins cher et suffisant pour notre formation

        messages=[
        # messages est une liste de messages
        # c'est comme une conversation avec le modèle

            {"role": "system", "content": styles[style]},
            # role "system" = instruction secrète pour le modèle
            # styles[style] récupère l'instruction du style choisi
            # exemple : styles["formel"] = "Tu es un expert..."

            {"role": "user", "content": f"Explique ce sujet en 3 phrases : {sujet}"}
            # role "user" = le message de l'utilisateur
            # f"..." insère la variable sujet dans le texte
        ]
    )

    return response.choices[0].message.content
    # on retourne uniquement le texte de la réponse
    # response.choices[0] = la première réponse du modèle
    # .message.content = le texte de cette réponse

# === TESTS DES 3 STYLES ===

sujet = "l'intelligence artificielle"
# on définit le sujet qu'on veut expliquer

print("=== STYLE FORMEL ===")
# on affiche un titre pour séparer les résultats
print(generer_contenu(sujet, "formel"))
# on appelle la fonction avec le style formel
print()
# print() sans argument affiche une ligne vide

print("=== STYLE VULGARISÉ ===")
print(generer_contenu(sujet, "vulgarise"))
print()

print("=== STYLE TECHNIQUE ===")
print(generer_contenu(sujet, "technique"))
# on appelle la fonction 3 fois avec 3 styles différents