from decimal import Decimal, ROUND_HALF_UP
from typing import List, Tuple

def investissement(
    capital_initial: float,
    taux_annuel_pct: float,
    nb_annees: int,
    versement_mensuel: float,
    versement_debut_mois: bool = True,
) -> List[Tuple[int, float]]:
    """
    Simule un investissement avec versements mensuels et intérêts composés.

    Paramètres
    ---------
    capital_initial : montant de départ (euros)
    taux_annuel_pct : taux annuel en pourcentage (ex. 5 pour 5%)
    nb_annees       : durée en années (entier >= 0)
    versement_mensuel : versement ajouté chaque mois (euros)
    versement_debut_mois : True = versement puis intérêts (début de mois)
                           False = intérêts puis versement (fin de mois)

    Retour
    ------
    Liste de tuples (annee, capital_arrondi_en_euros) à la fin de chaque année.
    """
    if nb_annees < 0:
        raise ValueError("nb_annees doit être >= 0")
    if versement_mensuel < 0:
        raise ValueError("versement_mensuel doit être >= 0")

    capital = Decimal(str(capital_initial))
    v_mensuel = Decimal(str(versement_mensuel))
    taux_mensuel = Decimal(str(taux_annuel_pct)) / Decimal("1200")

    rendements: List[Tuple[int, float]] = []

    for mois in range(1, nb_annees * 12 + 1):
        if versement_debut_mois:
            capital += v_mensuel
            capital *= (Decimal("1") + taux_mensuel)
        else:
            capital *= (Decimal("1") + taux_mensuel)
            capital += v_mensuel

        if mois % 12 == 0:
            annee = mois // 12
            capital_arrondi = capital.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
            rendements.append((annee, float(capital_arrondi)))

    return rendements


def investissement_mensuel(
    capital_initial: float,
    taux_annuel_pct: float,
    nb_annees: int,
    versement_mensuel: float,
    versement_debut_mois: bool = True,
):
    """Retourne la série mois par mois: liste de dicts avec 'mois_absolu', 'annee', 'mois', 'capital'"""
    capital = Decimal(str(capital_initial))
    v_mensuel = Decimal(str(versement_mensuel))
    taux_mensuel = Decimal(str(taux_annuel_pct)) / Decimal("1200")
    n = nb_annees * 12
    serie = []
    for m in range(1, n+1):
        if versement_debut_mois:
            capital += v_mensuel
            capital *= (Decimal("1") + taux_mensuel)
        else:
            capital *= (Decimal("1") + taux_mensuel)
            capital += v_mensuel
        annee = (m-1)//12 + 1
        mois = ((m-1)%12) + 1
        serie.append({
            "mois_absolu": m,
            "annee": annee,
            "mois": mois,
            "capital": float(capital.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))
        })
    return serie
