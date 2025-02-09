# For your imports look at the rulebook to see what is allowed
# Pour les import permis allez vous référer au livre des règlements
"""part_4.py
This is the template file for the part 4 of the Prelim 2.
Ceci est le fichier template pour la partie 4 du Prelim 2.
"""

def part_4(weights, positions):
    """
    Computes the position to balance a boat with passengers

    Parameters:
        weights [int]: The weight of all the passengers
        positions [float]: The position of all the passengers
    
    Returns:
        float or str: the position as a float or if it not valid the error string
    """
    error_message = "On CHATvire!"
    position = 0
    ### You code goes here ###
    ### Votre code va ici ###
    effect = 0
    for i in range(len(weights)):
        effect += weights[i]*positions[i]
    
    
    
    position = -effect/100
    if position == -0:
        position = 0
    if effect not in range(-50,50):
        position = error_message

    
    
        





    return position
print(part_4([0.5, -0.2, 0.5, -0.1], [40, 70, 70, 40]))