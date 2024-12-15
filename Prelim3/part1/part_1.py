# For your imports look at the rulebook to see what is allowed
# Pour les import permis allez vous référer au livre des règlements
"""part_1.py
This is the template file for the part 1 of the Prelim 3.
Ceci est le fichier template pour la partie 1 du Prelim 3.
"""

def part_1(genes) -> int:
    """
    Give the probability to herit a rececive disease

    Parameters:
        genes [str]: the genes from the patient and their ancestors

    Returns:
        float: the probability of having the rececive disease with 2 decimal precision
    """
    probability = 0.0
    ### You code goes here ###
    ### Votre code va ici ###
    tree = []
    rows = is_tree(len(genes))+1
    genes2 = genes[1:]
    print(genes2)
    for i in range(rows-1):
        tree.append([])
    
    tree[0].append(genes[0])
    
    for i in range(1,rows-1):
        print(tree)
        print(i)
        for j in range(len(tree[i-1])*2):
            tree[i].append(genes2[0])
            genes2.pop(0)
    for i in range(rows):
        u = int(((len(tree[-i])/2)))
        for j in range(u):
            if tree[-i][j*2] == "XX":
                print(tree[-i][j])
                if tree[-i][j*2+1].isupper():
                    print(tree[-i][j*2+1])
                elif tree[-i][j*2+1].islower():
                    print(tree[-i][j*2+1])
                else:
                    print(tree[-i][j*2+1])
                
            elif tree[-i] == tree[0]:
                break
            else:
                if tree[-i][j*2].isupper():
                    
                    print(tree[-i][j*2])
                    if tree[-i][j*2+1].isupper():
                        print(tree[-i][j*2+1])
                    elif tree[-i][j*2+1].islower():
                        print(tree[-i][j*2+1])
                    else:
                        print(tree[-i][j*2+1])
                elif tree[-i][j*2].islower():
                    print(tree[-i][j*2])
                    if tree[-i][j*2+1].isupper():
                        print(tree[-i][j*2+1])
                    elif tree[-i][j*2+1].islower():
                        print(tree[-i][j*2+1])
                    else:
                        print(tree[-i][j*2+1])
                else:
                    print(tree[-i][j*2])
                    if tree[-i][j*2+1].isupper():
                        print(tree[-i][j*2+1])
                    elif tree[-i][j*2+1].islower():
                        print(tree[-i][j*2+1])
                    else:
                        print(tree[-i][j*2+1])
                
                
            
    

    
    
    while True:
        break
        
            
        
    print(tree)
    
            






    return probability
    
    
def is_tree(xValue):
    num = 1
    nums = 1
    rows = 0
    while True:
        if xValue <= nums:
            break
        
        else:
            nums = nums + num*2
            num = num*2
            rows += 1
    return rows+1


    


part_1(["XX", "XX", "XX", "XX", "Tt", "tt", "XX", "TT", "TT", "Tt", "Tt", "Tt", "XX", "TT", "tt"])
