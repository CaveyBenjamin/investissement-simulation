# Simulation d’investissement (Python)

Ce projet simule l’évolution d’un capital avec :
- un **capital initial**
- des **versements mensuels**
- un **taux d’intérêt annuel** (converti en taux mensuel)
- **intérêts composés**

## Aperçu du graphique
![Évolution du capital](assets/evolution_capital.png)

## Installation (optionnelle, pour exécuter le notebook)
```bash
pip install -r requirements.txt
```

## Utilisation rapide
```python
from src.investissement import investissement

resultat = investissement(1000, 5, 10, 100, True)  # 1000€, 5%/an, 10 ans, 100€/mois, versement en début de mois
for annee, valeur in resultat:
    print(f"Année {annee} : {valeur:.0f} €")
```

## Détails techniques
- **Convention** : `versement_debut_mois=True` (versement puis intérêts). Mettre `False` pour **fin de mois** (intérêts puis versement).
- **Taux mensuel** : `taux_annuel / 12 / 100`
- Version **mensuelle** disponible via `investissement_mensuel(...)` (retourne une liste d’enregistrements).

## Structure
```
.
├─ notebooks/
│  └─ simulation_investissement.ipynb
├─ src/
│  └─ investissement.py
├─ assets/
│  └─ evolution_capital.png
├─ README.md
└─ requirements.txt
```

## Licence
MIT (à adapter si besoin).
