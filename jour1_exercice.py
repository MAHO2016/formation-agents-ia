# Calculateur de devis pour agents IA
# ComptaProgresso — Formation Agents IA

# === FONCTION PRINCIPALE ===
def calculer_devis(nom_client, nom_agent, prix_mensuel, nombre_mois, remise=0):
    # remise=0 signifie : pas de remise par défaut

    sous_total = prix_mensuel * nombre_mois
    # Calcul du sous-total

    montant_remise = sous_total * remise
    # Calcul du montant de la remise (0 si pas de remise)

    sous_total_apres_remise = sous_total - montant_remise
    # Sous-total après déduction de la remise

    tva = sous_total_apres_remise * 0.18
    # TVA à 18% sur le montant après remise

    total = sous_total_apres_remise + tva
    # Total final

    print(f"=== DEVIS POUR {nom_client} ===")
    print(f"Agent        : {nom_agent}")
    print(f"Prix mensuel : {prix_mensuel} EUR x {nombre_mois} mois")
    print(f"Sous-total   : {round(sous_total, 2)} EUR")
    if remise > 0:
        print(f"Remise ({int(remise*100)}%) : -{round(montant_remise, 2)} EUR")
    print(f"TVA (18%)    : {round(tva, 2)} EUR")
    print(f"TOTAL        : {round(total, 2)} EUR")
    print()

# === TESTS ===
# Test 1 — sans remise
calculer_devis("M. Odilon", "Assistant Comptable Pro", 150, 3)

# Test 2 — avec 10% de remise
calculer_devis("Mme Diallo", "Agent de Veille Sectorielle", 200, 12, remise=0.10)

# Test 3 — abonnement court
calculer_devis("M. Ahouansou", "Chatbot FAQ Etudiant", 100, 1)

# === BONUS : CATÉGORIE CLIENT ===
def categoriser_client(total):
    if total < 1000:
        return "Standard"
    elif total <= 5000:
        return "Premium"
    else:
        return "Enterprise"

# Test de la catégorisation
print(f"M. Odilon    → {categoriser_client(531.0)}")
print(f"Mme Diallo   → {categoriser_client(2548.8)}")
print(f"M. Ahouansou → {categoriser_client(118.0)}")