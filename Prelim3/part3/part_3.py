# For your imports look at the rulebook to see what is allowed
# Pour les import permis allez vous référer au livre des règlements
"""part_3.py
This is the template file for the part 3 of the Prelim 3.
Ceci est le fichier template pour la partie 3 du Prelim 3.
"""

def part_3(systolic: int, diastolic: int, heart_rate: int):
    """
    Generate display of heart monitor for 4 heartbeats

    Parameters:
        systolic int: The systolic value
        diastolic int: the diastolic value
        heart_rate int: the heart rate

    Returns:
        [str]: The array of strings composing the monitor for 4 heartbeats
    """
    monitor = []
    ### You code goes here ###
    ### Votre code va ici ###
    systolic_lines = systolic // 20
    diastolic_lines = diastolic // 20
    neutral_lines = (180 - heart_rate) // 10
    neutral = "| |_   "
    monitor = []

    for i in range(neutral_lines):
        neutral = neutral + "_"

    spaces = len(neutral) - 3
    top = " _ "
    up = "| |"
    down = "    | |"
    bottom = "    |_|"
    for j in range(spaces):
        up = up + " "
        top = top + " "

    for k in range(spaces - 4):
        down = down + " "
        bottom = bottom + " "

    monitor.append(top)
    for l in range(systolic_lines - 1):
        monitor.append(up)

    monitor.append(neutral)
    for m in range(diastolic_lines - 1):
        monitor.append(down)

    monitor.append(bottom)
    for n in range(len(monitor)):
        for o in range(2):
            monitor[n] = monitor[n] + monitor[n]
    for p in monitor:
        print(p)


    return monitor
