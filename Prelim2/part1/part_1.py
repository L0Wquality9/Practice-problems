# For your imports look at the rulebook to see what is allowed
# Pour les import permis allez vous référer au livre des règlements
"""part_1.py
This is the template file for the part 1 of the Prelim 2.
Ceci est le fichier template pour la partie 1 du Prelim 2.
"""

def part_1(equation: str) -> int:
    """
    Solve a simple CAT math equation

    Parameters:
        equation str: the equation to solve using CAT math

    Returns:
        int: the solution to the CAT math equation
    """
    result = 0
    ### You code goes here ###
    ### Votre code va ici ###
    
    
    for i in range(len(equation)): 
        
        if equation[i] == "+":
            result = equation[:i] + equation[i+1:]
        elif equation[i] == "*":
            for t in range(int(equation[i+1:])):
                result = str(result) + str(equation[:i])
            result = int(result)

    

    return result

