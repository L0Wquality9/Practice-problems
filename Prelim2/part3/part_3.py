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
    for i in range(len(word_2) + 2):
        grid.append([])
    
        for t in range(len(word_1) + 2):
            
            grid[i].append(0)
    grid[1][1] = 0
    for i in range(len(grid)-2):
        grid[i+2][0]=word_2[i]
    for i in range(len(word_1)):
        grid[0][i+2] = word_1[i]
    for i in grid:
        print(*i)
    
    for i in range(len(word_1)):
        grid[1][i+2] = grid[1][i+1]+1
    for i in range(len(word_2)):
        grid[i+2][1] = grid[i+1][1]+1
    string = []
    for i in range(len(word_1)+2):
        string.append("-")
    print(*string)
    if len(word_1)>len(word_2):
        
        for t in range(len(word_2)):
            for i in range(len(word_1)):
                if i+1>len(word_2):
                    grid[t+2][i+2] = grid[t+2][i+1]+1
                elif word_1[i]!=word_2[t]:
                    grid[t+2][i+2] = grid[t+1][i+1]+1
                elif word_1[i]==word_2[i]:
                    grid[t+2][i+2] = grid[t+1][i+1]
            for p in grid:
                print(*p)
            print(*string)
        
        
    else:
        pass
    
            
    for i in grid:
        print(*i)
    


    return CAPTCHA
part_3(words=["sitting", "kitten"])