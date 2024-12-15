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
    rows = is_tree(len(genes))+1
    tree = create_tree(genes, rows)
    
    for i in range(rows):
        u = int(((len(tree[-i])/2)))
        for j in range(u):
            
                if isinstance(tree[-i][j*2], int or float):
                    pass
                
            
                
                elif tree[-i][j*2] == "XX":
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
                            tree = bothUpper(tree, i, j)
                            print(tree[-i][j*2+1])
                        elif tree[-i][j*2+1].islower():
                            tree = upperLower(tree, i, j)
                            print(tree[-i][j*2+1])
                        else:
                            tree = case4(tree, i, j)
                            print(tree[-i][j*2+1])
                    elif tree[-i][j*2].islower():
                        print(tree[-i][j*2])
                        if tree[-i][j*2+1].isupper():
                            upperLower(tree, i, j)
                            print(tree[-i][j*2+1])
                        elif tree[-i][j*2+1].islower():
                            bothLower(tree, i, j)
                            print(tree[-i][j*2+1])
                        else:
                            case3(tree, i, j)
                            print(tree[-i][j*2+1])
                    else:
                        print(tree[-i][j*2])
                        if tree[-i][j*2+1].isupper():
                            print(tree[-i][j*2+1])
                            case4(tree, i, j)
                        elif tree[-i][j*2+1].islower():
                            print(tree[-i][j*2+1])
                            case3(tree, i, j)
                        else:
                            upperLower(tree, i, j)
                            print(tree[-i][j*2+1])
                
                
            
    

    
    
    while True:
        break
        
            
        
    for i in tree:
        print(*i)
    
            






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

def create_tree(genes, rows):
    tree = []
    
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
    return tree
def bothUpper(tree, i, j):
    tree[-i-1][j] = 0
    print(tree)
    return tree
def bothLower(tree, i, j):
    tree[-i-1][j] = 100
    return tree
#case 3 is 1 all lower and one both
def case3(tree, i, j):
    tree[-i-1][j] = 12.5
    return tree
#case 4 is 1 all upper and one both
def case4(tree, i, j):
    tree[-i-1][j] = 25
    return tree
def upperLower(tree, i, j):
    tree[-i-1][j] = 25
    return tree
    


part_1(["XX", "Cc", "cc"])
