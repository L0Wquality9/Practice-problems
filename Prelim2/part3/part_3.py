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
    for i in range(len(grid)-2):
        print(i)
        print(len(grid[i]))
        for j in range(len(grid[i])-2):
            print(j)
            print(word_2[i])
            print(word_1[j])
            if min(i,j)==0:
                grid[i+2][j+2] = max(i,j)+1
            else:
                if word_2[i] != word_1[j]:
                    
                    grid[i+2][j+2] = min((grid[i+1][j+2]+1), (grid[i+2][j+1]+1), (grid[i+1][j+1]+1))
                    print(str(i) + " is i, " + str(j)+" is j")
                else:
                    grid[i+2][j+2] = min((grid[i+1][j+2]+1), (grid[i+2][j+1]+1), (grid[i+1][j+1]))
                    print( str(j)+" is j, "+str(i) + " is i")
                for t in grid:
                    print(*t)
    
    
    
    print(*string)     
    for t in grid:
        print(*t)
    distance = grid[-1][-1]
    faceNum = distance%4
    print(faceNum)
    if faceNum == 0:
        face = [" ^-^ ","|'_'|"," > < "]
    elif faceNum == 1:
        face = [" ^-^ ","|-_-|"," > < "]
    elif faceNum == 2:
        face = [" ^-^ ","|*_*|"," > < "]
    else:
        face = [" ^-^ ","|@_@|"," > < "]
    
    for i in face:
        print(*i)

    
    


    return CAPTCHA
part_3(words=["kitten", "sitting"])