import os
# Permet d'accéder aux variables d'environnement

import csv
# Pour écrire le fichier CSV final

from datetime import datetime
# Pour récupérer la date du jour automatiquement

from dotenv import load_dotenv
# Pour charger le fichier .env

from openai import OpenAI
# La classe pour parler à l'API OpenAI

# Charger les variables du fichier .env
load_dotenv()

# Créer la connexion à l'API
client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))

print("Connexion API réussie ! On peut commencer.")

# === BLOC 1 : FEW-SHOT PROPOSITION COMMERCIALE ===
def few_shot_proposition(secteur):
    # Cette fonction génère une proposition commerciale courte
    # en se basant sur 3 exemples (few-shot)

    response = client.chat.completions.create(
        model='gpt-3.5-turbo',
        max_tokens=80,
        temperature=0.7,
        messages=[
            {
                'role': 'system',
                'content': 'Tu es un commercial expert qui propose des agents IA '
                            'aux entreprises africaines. Tu rédiges des propositions '
                            'courtes, concrètes et percutantes en 2 phrases maximum.'
            },
            # Exemple 1
            {'role': 'user',      'content': 'Secteur : Comptabilité'},
            {'role': 'assistant', 'content': 'Notre agent IA automatise vos rapports '
                                              'comptables et detecte les erreurs en temps reel. '
                                              'Gagnez 10h par semaine.'},
            # Exemple 2
            {'role': 'user',      'content': 'Secteur : Agriculture'},
            {'role': 'assistant', 'content': 'Notre agent IA analyse vos donnees de recolte '
                                              'et predit les meilleurs moments de vente. '
                                              'Augmentez vos revenus de 20%.'},
            # Exemple 3
            {'role': 'user',      'content': 'Secteur : Sante'},
            {'role': 'assistant', 'content': 'Notre agent IA aide vos medecins a trier '
                                              'les urgences et organiser les rendez-vous. '
                                              'Reduisez les temps d\'attente de 30%.'},
            # Vraie question
            {'role': 'user', 'content': f'Secteur : {secteur}'}
        ]
    )
    return response.choices[0].message.content

# === TEST DU BLOC 1 ===
print()
print("=== TEST FEW-SHOT ===")
print(few_shot_proposition("Education"))

# === BLOC 2 : PITCH MULTI-STYLE ===
def generer_pitch(sujet, style):
    # Cette fonction génère un pitch de vente
    # adapté à 3 audiences différentes

    styles = {
        'client_direct': (
            'Tu es un commercial qui parle directement à un patron de PME africaine. '
            'Utilise un langage simple, concret, axé sur les bénéfices immédiats '
            'et le retour sur investissement.'
        ),
        'investisseur': (
            'Tu es un entrepreneur qui pitch à un investisseur. '
            'Utilise un langage axé sur le marché, la scalabilité, '
            'les chiffres et le potentiel de croissance.'
        ),
        'partenaire_tech': (
            'Tu es un developpeur qui presente a un partenaire technique. '
            'Utilise un langage technique : architecture, API, '
            'integration, stack technologique.'
        )
    }

    response = client.chat.completions.create(
        model='gpt-3.5-turbo',
        max_tokens=150,
        temperature=0.7,
        messages=[
            {'role': 'system', 'content': styles[style]},
            {'role': 'user',   'content': f'Fais un pitch en 2-3 phrases pour : {sujet}'}
        ]
    )
    return response.choices[0].message.content


# === TEST DU BLOC 2 ===
print()
print("=== TEST MULTI-STYLE ===")
sujet_test = "un agent IA qui automatise la comptabilité des PME"

for style in ['client_direct', 'investisseur', 'partenaire_tech']:
    print(f"--- Style: {style} ---")
    print(generer_pitch(sujet_test, style))
    print()

# === BLOC 3 : GÉNÉRATION COMPLÈTE + SAUVEGARDE CSV ===
def generer_catalogue_commercial(sujets):
    # sujets = liste de sujets à traiter
    # Pour chaque sujet, on génère :
    #   - 1 proposition few-shot (secteur)
    #   - 3 pitchs multi-style (client_direct, investisseur, partenaire_tech)

    resultats = []
    date_du_jour = datetime.now().strftime('%Y-%m-%d')
    # Récupère la date d'aujourd'hui au format AAAA-MM-JJ

    for sujet in sujets:
        # --- Partie few-shot ---
        proposition = few_shot_proposition(sujet)
        resultats.append([date_du_jour, sujet, 'few_shot_secteur', proposition])
        print(f"Proposition few-shot generee pour : {sujet}")

        # --- Partie multi-style ---
        for style in ['client_direct', 'investisseur', 'partenaire_tech']:
            pitch = generer_pitch(sujet, style)
            resultats.append([date_du_jour, sujet, style, pitch])
            print(f"Pitch '{style}' genere pour : {sujet}")

    # --- Sauvegarde dans le CSV ---
    with open('catalogue_commercial.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Date', 'Sujet', 'Style', 'Contenu'])
        # Ligne d'en-tête

        writer.writerows(resultats)
        # Toutes les lignes de résultats en une fois

    print()

    print(f"{len(resultats)} lignes sauvegardees dans catalogue_commercial.csv !")

# === EXÉCUTION FINALE ===
print()
print("=== GENERATION DU CATALOGUE COMMERCIAL ===")

sujets_a_traiter = [
    "Education",
    "Transport et logistique"
]

generer_catalogue_commercial(sujets_a_traiter)