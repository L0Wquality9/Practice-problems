# For your imports look at the rulebook to see what is allowed
# Pour les import permis allez vous référer au livre des règlements
"""part_2.py
This is the template file for the part 2 of the Prelim 2.
Ceci est le fichier template pour la partie 2 du Prelim 2.
"""

def part_2(d: int, h: int, b: int, m_cost: float, margin: float) -> float:
    """
    Computes the profit of custom made top hats
    
    Parameters:
        d int: the width of the opening of the hat
        h int: the height of the hat
        b int: the width of the brim
        m_cost float: the cost of the material
        margin float: the profit margin you want to make

    Returns:
        float: the profit for the custom hat
    """
    profit = 0
    ### You code goes here ###
    ### Votre code va ici ###
    import math
    top = math.pi * (d/2)**2
    side = 2 * math.pi * (d/2) * h
    brim = math.pi * (b + (d/2))**2 - math.pi * (d/2)**2
    materials = top + side + brim
    profit = round(materials * m_cost * margin, 2)

    return profit

