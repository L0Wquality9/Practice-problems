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

    #creating grid with letters and first row and column of numbers
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
    
    
    for i in range(len(word_1)):
        grid[1][i+2] = grid[1][i+1]+1
    for i in range(len(word_2)):
        grid[i+2][1] = grid[i+1][1]+1
    
    

    #filling in the grid
    for i in range(len(grid)-2):
        
        for j in range(len(grid[i])-2):
            
            if min(i,j)==0:
                grid[i+2][j+2] = max(i,j)+1
            else:
                if word_2[i] != word_1[j]:
                    
                    grid[i+2][j+2] = min((grid[i+1][j+2]+1), (grid[i+2][j+1]+1), (grid[i+1][j+1]+1))
                    
                else:
                    grid[i+2][j+2] = min((grid[i+1][j+2]+1), (grid[i+2][j+1]+1), (grid[i+1][j+1]))
                    
                
                    
    
    
    
    
    
    #finding right face
    distance = grid[-1][-1]
    faceNum = distance%4
    
    if faceNum == 0:
        face = [" ^-^ ","|'_'|"," > < "]
    elif faceNum == 1:
        face = [" ^-^ ","|-_-|"," > < "]
    elif faceNum == 2:
        face = [" ^-^ ","|*_*|"," > < "]
    else:
        face = [" ^-^ ","|@_@|"," > < "]
    
    

    #Finding subs, deletions, insertions
    posX = -1
    posY = -1
    lenX = len(word_1)
    
    replaceLetter = []
    replacePos = []
    deletePos = []
    deleteLetter = []
    insertLetter = []
    insertPos = []

    while True:
        
        if all(x > grid[posY-1][posX-1] for x in [grid[posY-1][posX],grid[posY][posX-1]]):
            
            if grid[posY-1][posX-1] != grid[posY][posX]:
                replacePos.append(lenX+posX)
                replaceLetter.append(word_1[lenX+posX])
            posY = posY-1
            posX = posX-1
        elif all(x > grid[posY][posX-1] for x in [grid[posY-1][posX],grid[posY-1][posX-1]]):
            
            
            insertPos.append(lenX+posX)
            insertLetter.append(word_1[lenX+posX])
                
            posY = posY
            posX = posX-1
        else:
            
            deletePos.append(lenX+posX)
            

            posY = posY-1
            posX = posX
        if abs(posX) == len(grid[0])-1 and abs(posY) == len(grid)-1:
            break

    

    #Doing opperations on the face
    faceReplace = []
    faceDelete = []
    faceInsert = []
    for i in range(len(face[2])):
            faceReplace.append(face[2][i])
    for i in range(len(replaceLetter)):
        replacePosIn = replacePos[i]%5
        faceReplace[replacePosIn] = replaceLetter[i]
        
    face[2] = faceReplace
        
    
    
        
        
    for i in range(len(face[1])):
           faceDelete.append(face[1][i])
    for i in range(len(deletePos)):
           deletePosIn = deletePos[i]%5
           faceDelete.pop(deletePosIn)
    face[1] = faceDelete
        
    
    for i in range(len(face[0])):
        faceInsert.append(face[0][i])
    for i in range(len(insertLetter)):
        insertPosIn = insertPos[i]%5
        insertPosIn = int(insertPosIn)
        faceInsert.insert(insertPosIn,insertLetter[i])
    face[0] = faceInsert

    for i in face:
        print(*i)


    
    


    return CAPTCHA
part_3(words=["pun'ctu/ation", "pon~ctuat'ion"])