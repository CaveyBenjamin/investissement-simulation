def investissement(capital_initial, taux_annuel, duree, versement_mensuel):
    capital = capital_initial
    rendements = []
    taux_mensuel = taux_annuel / 12 / 100  
    for mois in range(1, duree * 12 + 1):
        capital += versement_mensuel
        capital *= (1 + taux_mensuel)
        if mois % 12 == 0:
            annee = mois // 12
            rendements.append((annee, capital))

    return rendements
resultat = investissement(1000, 5, 10, 100)
for annee, valeur in resultat:
    print(f"Année {annee} : {valeur:.0f} €")
