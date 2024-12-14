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
    
    
    num_Yy = 0
    num_YY = 0
    num_yy = 0
    num_XX = 0
    yValue = 0
    for i in genes:
        if i == 'XX':
            num_XX += 1
        else:
            if i.islower():
                num_yy += 1
                yValue += 2
            elif i.isupper():
                num_YY += 1
            else:
                num_Yy += 1
                yValue += 1
    if is_tree(num_XX):
        probability = float(num_XX/yValue/4*100)
        print("is tree")
    else:
        probability = float(num_XX/yValue/2*100)
        print('not tree')


    
    print(probability)
    thing = list((num_Yy, num_yy, num_YY, num_XX, yValue))
    print(thing)



    return probability
    
    
def is_tree(xValue):
    num = 1
    nums = 1
    while True:
        if xValue <= nums:
            break
        
        else:
            nums = nums + num*2
            num = num*2
    if nums == xValue:
        return True
    else:
        return False



    


