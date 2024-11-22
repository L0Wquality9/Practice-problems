# For your imports look at the rulebook to see what is allowed
# Pour les import permis allez vous référer au livre des règlements
"""part_3.py
This is the template file for the part 3 of the Prelim 2.
Ceci est le fichier template pour la partie 3 du Prelim 2.
"""

def part_3(words):
    """
    Generate a CAPTCHA from the Levenstein distance of 2 words

    Parameters:
        words [string]: the 2 words from which you will need to find the distance

    Returns:
        [str]: The array of strings composing the CAPTCHA
    """
    CAPTCHA = []

    ### You code goes here ###
    ### Votre code va ici ###
    grid = []
    word_1 = words[0]
    word_2 = words[1]
    for i in range(len(word_2) + 1):
        grid.append([])
    
        for t in range(len(word_1) + 1):
            print(t)
            grid[i].append("")
    grid[0][0] = "0"
    for i + 1 in range(len(word_2) - 1):
        if word_1[i] == word_2[i]:
            pass
            
    for i in grid:
        print(i)
    


    return CAPTCHA
part_3(words=["aword", "this"])