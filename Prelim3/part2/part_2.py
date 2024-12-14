# For your imports look at the rulebook to see what is allowed
# Pour les import permis allez vous référer au livre des règlements
"""part_2.py
This is the template file for the part 2 of the Prelim 3.
Ceci est le fichier template pour la partie 2 du Prelim 3.
"""
proba_full = {
    .10: [.02, .00, .00, .00, .00, .00],
    .20: [.07, .02, .00, .00, .00, .00],
    .30: [.14, .07, .04, .02, .01, .00],
    .40: [.23, .14, .09, .06, .04, .03],
    .50: [.33, .24, .17, .13, .10, .08],
    .55: [.39, .29, .23, .18, .14, .11],
    .60: [.45, .35, .29, .24, .20, .17],
    .65: [.51, .42, .35, .30, .26, .21],
    .70: [.57, .51, .43, .38, .34, .30],
    .75: [.64, .57, .51, .46, .42, .39],
    .80: [.71, .65, .60, .55, .52, .49],
    .85: [.78, .73, .69, .65, .62, .60],
    .90: [.85, .83, .79, .76, .74, .72],
    .95: [.92, .91, .89, .88, .87, .85]
}

def part_2(arrivals: int, mu: int, c: int) -> float:
    """
    Computes the total wait time at the CRC hospital
    
    Parameters:
        arrivals int: the width of the opening of the hat
        mu int: the height of the hat
        c int: the width of the brim

    Returns:
        float: temps d'attente en minutes
    """
    wait_time_minutes = 0
    ### You code goes here ###
    ### Votre code va ici ###
    rho = arrivals / (c * mu)
    if rho >= 1:
        return float('inf')
    rho_key = round(rho, 2)
    if rho_key not in proba_full:
        rho_key = round(rho, 1)
    P_full = proba_full[rho_key][c - 2]
    Lq = (P_full * rho) / (1 - rho)
    L = (arrivals / mu) + Lq
    W = L / arrivals
    print(round(W * 60, 2))
    wait_time_minutes = round(W * 60, 2)

    return wait_time_minutes
