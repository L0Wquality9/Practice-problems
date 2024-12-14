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
                    if k not in j[1]:
                        symptomes.remove(k)
    print(symptomes)
    for i in diagnostics:
        
        if all(elements in i[1] for elements in symptomes):
            diagnostic = i[0]
            


    print(diagnostic)
    return diagnostic
