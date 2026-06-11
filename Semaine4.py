import os
# os permet d'accéder au système d'exploitation

from dotenv import load_dotenv
# load_dotenv est la fonction qui lit le fichier .env
# et charge les variables qu'il contient

from openai import OpenAI
# on importe la classe OpenAI pour parler à l'API

load_dotenv()
# cette fonction lit le fichier .env
# et charge OPENAI_API_KEY dans les variables d'environnement

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
# on crée la connexion avec l'API
# os.environ.get() lit la clé depuis les variables d'environnement

print("Connexion API réussie !")
# on affiche un message pour confirmer que tout fonctionne

def few_shot_exemple():
    # on envoie plusieurs messages pour montrer des exemples au modèle
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        # on choisit le modèle

        messages=[
            {"role": "system", "content": "Tu es un expert en marketing digital en Afrique de l'Ouest."},
            # instruction principale : définit le rôle du modèle

            {"role": "user", "content": "Crée un slogan pour une application de livraison."},
            # premier exemple — question

            {"role": "assistant", "content": "Livré chez vous, rapide comme l'éclair !"},
            # premier exemple — réponse attendue
            # on montre au modèle le style de réponse qu'on veut

            {"role": "user", "content": "Crée un slogan pour une application de paiement mobile."},
            # deuxième exemple — question

            {"role": "assistant", "content": "Payez partout, en toute simplicité !"},
            # deuxième exemple — réponse attendue
            # le modèle comprend maintenant le style court et percutant

            {"role": "user", "content": "Crée un slogan pour une application de formation en ligne."},
            # vraie question — le modèle va imiter le style des exemples
        ]
    )
    return response.choices[0].message.content
    # on retourne uniquement le texte de la réponse

print("=== FEW-SHOT PROMPTING ===")
# on affiche un titre pour séparer les résultats

print(few_shot_exemple())
# on appelle la fonction et on affiche le résultat

import csv
# on importe le module CSV pour écrire les résultats

def generer_et_sauvegarder(sujet):
    # fonction qui génère le contenu en 3 styles
    # et sauvegarde les résultats dans un fichier CSV

    styles = {
        "formel": "Tu es un expert professionnel. Explique de façon formelle.",
        # style académique et soutenu

        "vulgarise": "Tu es un vulgarisateur. Explique simplement comme à un enfant de 12 ans.",
        # style simple et accessible

        "technique": "Tu es un ingénieur expert. Explique de façon très technique."
        # style précis pour les experts
    }

    resultats = []
    # liste vide qui va stocker les résultats des 3 styles

    for style, instruction in styles.items():
        # on parcourt chaque style du dictionnaire
        # style = nom du style (formel, vulgarise, technique)
        # instruction = le texte de l'instruction

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": instruction},
                # on injecte l'instruction du style actuel

                {"role": "user", "content": f"Explique en 2 phrases : {sujet}"}
                # on demande une explication courte pour économiser les tokens
            ]
        )

        contenu = response.choices[0].message.content
        # on récupère le texte de la réponse

        resultats.append([sujet, style, contenu])
        # on ajoute une ligne dans la liste : [sujet, style, contenu]

        print(f"✓ Style {style} généré")
        # on affiche une confirmation pour chaque style

    with open("resultats.csv", "w", newline="", encoding="utf-8") as fichier:
        # on ouvre le fichier CSV en mode écriture
        # encoding="utf-8" pour supporter les accents

        writer = csv.writer(fichier)
        # on crée un objet writer pour écrire dans le fichier

        writer.writerow(["Sujet", "Style", "Contenu"])
        # on écrit la ligne d'en-tête du CSV

        writer.writerows(resultats)
        # on écrit toutes les lignes de résultats en une seule fois

    print("\nRésultats sauvegardés dans resultats.csv !")
    # on confirme que le fichier a été créé

# on appelle la fonction avec un sujet
generer_et_sauvegarder("les agents IA en Afrique")