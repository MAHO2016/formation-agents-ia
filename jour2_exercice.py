# Liste des candidats ComptaProgresso
# Chaque candidat : [nom, UE préparée, note de contrôle continu]
candidats = [
    ['Kouassi Amed',    'UE1 DSCG',  14],
    ['Diallo Fatoumata','UE4 DSCG',  8],
    ['Ahouansou Eric',  'DCG UE9',   16],
    ['Zinsou Marie',    'UE1 DSCG',  11],
    ['Kone Ibrahim',    'UE4 DSCG',  7],
    ['Mensah Sandra',   'DCG UE9',   13],
    ['Bah Mamadou',     'UE1 DSCG',  9],
    ['Toure Aminata',   'DCG UE9',   18],
]

print(f'Nombre total de candidats : {len(candidats)}')

# === ÉTAPE 1 : LISTE COMPLÈTE ===
print()
print("=== LISTE COMPLÈTE DES CANDIDATS ===")
for candidat in candidats:
    nom  = candidat[0]
    ue   = candidat[1]
    note = candidat[2]
    print(f"{nom} — {ue} — Note : {note}/20")

# === ÉTAPE 2 : CANDIDATS ADMIS ===
print()
print("=== CANDIDATS ADMIS (note >= 10) ===")
for candidat in candidats:
    if candidat[2] >= 10:
        print(f"{candidat[0]} — {candidat[1]} — {candidat[2]}/20")


# === ÉTAPE 3 : FILTRER PAR UE ===
def filtrer_par_ue(candidats, ue):
    print(f"=== CANDIDATS {ue} ===")
    for candidat in candidats:
        if candidat[1] == ue:
            statut = "Admis" if candidat[2] >= 10 else "Ajourné"
            print(f"{candidat[0]} — {candidat[2]}/20 — {statut}")
    print()

# Test de la fonction
filtrer_par_ue(candidats, "UE1 DSCG")
filtrer_par_ue(candidats, "UE4 DSCG")
filtrer_par_ue(candidats, "DCG UE9")

# === ÉTAPE 4 : MOYENNES ===
def calculer_moyenne(candidats, ue=None):
    if ue:
        notes = [c[2] for c in candidats if c[1] == ue]
        label = ue
    else:
        notes = [c[2] for c in candidats]
        label = "Générale"

    moyenne = sum(notes) / len(notes)
    print(f"Moyenne {label} : {round(moyenne, 2)}/20")

print("=== MOYENNES ===")
calculer_moyenne(candidats)
calculer_moyenne(candidats, "UE1 DSCG")
calculer_moyenne(candidats, "UE4 DSCG")
calculer_moyenne(candidats, "DCG UE9")

# === ÉTAPE 5 : CLASSEMENT GÉNÉRAL ===
print()
print("=== CLASSEMENT GÉNÉRAL ===")
classement = sorted(candidats, key=lambda c: c[2], reverse=True)

for rang, candidat in enumerate(classement):
    print(f"{rang+1}. {candidat[0]} — {candidat[1]} — {candidat[2]}/20")