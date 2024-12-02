# For your imports look at the rulebook to see what is allowed
# Pour les import permis allez vous référer au livre des règlements
"""part_4.py
This is the template file for the part 4 of the Prelim 3.
Ceci est le fichier template pour la partie 4 du Prelim 3.
"""

def part_4(symptomes, prescriptions, diagnostics, medicaments):
    """
    Computes the position to balance a boat with passengers

    Parameters:
        symptomes [str]: The list of symptomes
        prescriptions [str]: The list of prescritpions of the patient
        diagnostics [[str]]: The list of possible diagnostic with their effects
        medicaments [[str]]: The list of prescriptions possible with their side effects
    
    Returns:
        str: The diagnostic for the patient
    """
    diagnostic = ""
    ### You code goes here ###
    ### Votre code va ici ###
    for i in prescriptions:
        #print(i)
        for j in medicaments:
            #print(j[0])
            if i == j[0]:
                for k in symptomes:
                    if k in j[1]:
                        symptomes.remove(k)
    for i in diagnostics:
        if all(elements in i[1] for elements in symptomes):
            diagnostic = i[0]
            



    return diagnostic
diagnostics=[["Diabète", ["Déshydratation", "Gain de poids", "Perte de poids", "Besoin d'uriner", "Fatigue", "Troubles de vision", "Infections", "Picotements/Engourdissements des extrémités"]],
             ["COVID-19", ["Maux de gorge", "Écoulement nasal", "Éternuements", "Toux", "Fièvre", "Difficultés respiratoires", "Frissons", "Fatigue", "Maux de tête", "Douleurs musculaires", "Perte de l'odorat/du goût"]],
             ["Grippe", ["Toux", "Fièvre", "Douleurs musculaires", "Frissons", "Fatigue", "Maux de gorge", "Maux de tête", "Perte d'appétit", "Écoulement nasal", "Congestion nasale"]],
             ["Rhume", ["Toux", "Fatigue", "Éternuements", "Écoulement nasal", "Congestion nasale", "Maux de gorge"]],
             ["Sclérose en plaques", ["Dépression", "Douleurs", "Faiblesse", "Fatigue", "Intolérance à la chaleur", "Troubles de vision", "Troubles d'équilibre"]],
             ["Syphilis", ["Maux de tête", "Étourdissements", "Troubles de vision", "Troubles d'équilibre", "Troubles de coordination", "Démence", "Perte auditive"]],
             ["Gastroentérite", ["Diarrhée", "Douleurs abdominales", "Nausées", "Vomissements", "Fièvre", "Maux de tête", "Douleurs musculaires", "Perte d'appétit"]],
             ["Mononucléose", ["Fièvre", "Frissons", "Fatigue", "Perte d'appétit", "Douleurs musculaires", "Maux de tête", "Difficultés à avaler"]],
             ["Anémie", ["Pâleur", "Essoufflements", "Fatigue", "Palpitations", "Maux de tête", "Étourdissements", "Faiblesse", "Difficultés à se concentrer"]],
             ["Tuberculose", ["Toux", "Douleurs thoraciques", "Faiblesse", "Fatigue", "Perte de poids", "Perte d'appétit", "Frissons", "Fièvre", "Sueurs nocturnes"]],
             ["Maladie coeliaque", ["Douleurs abdominales", "Diarrhée", "Constipation", "Fatigue", "Dépression"]]
            ]

medicaments=[["Fluvoxamine", ["Nausées", "Insomnie", "Somnolence", "Céphalées", "Étourdissements", "Constipation", "Sécheresse de la bouche", "Vomissements"]],
             ["Antibiotiques", ["Diarrhée", "Fièvre", "Douleurs abdominales", "Perte d'appétit", "Déshydratation", "Nausées"]],
             ["Acétaminophène", ["Sécheresse de la bouche", "Maux de tête", "Étourdissements"]],
             ["Ibuprofène", ["Démangeaisons", "Insomnie", "Nausées", "Vomissements", "Douleurs/Crampes d'estomac", "Diarrhée", "Fatigue", "Indigestion", "Constipation", "Ballonnements"]]
            ]
part_4(["Troubles de vision", "Étourdissements", "Maux de tête", "Perte de poids"], ["Acétaminophène"], diagnostics, medicaments)