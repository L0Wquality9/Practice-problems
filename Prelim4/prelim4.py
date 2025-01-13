# For your imports look at the rulebook to see what is allowed
# Pour les import permis allez vous référer au livre des règlements
"""prelim4.py
This is the template file for Prelim4.
Ceci est le fichier template pour le problème Prelim4.
"""

def distance_manhattan(city_a: tuple[int,int], city_b: tuple[int,int]) -> int:
    distance = 0
    ## Your code goes here ###
    abs(city_a[0] - city_b[0]) + abs(city_a[1] - city_b[1])

    return distance


def get_stations(map: list[list[int]], n: int) -> list[tuple[int, int]]:
    stations = []
    ### Your code goes here ###
    for i in range(n):
        for j in range(n):
            if map[i][j] == 1:
                stations.append((i,j))


    return stations

def get_customers(map: list[list[int]], n: int) -> list[tuple[int, int]]:
    customers = []
    ### Your code goes here ###
    for i in range(n):
        for j in range(n):
            if map[i][j] == 2:
                customers.append((i,j))

    return customers


def solve(map: list[list[int]], n: int) -> list[list[tuple[int, int]]]:
    solution = []
    ### Your code goes here ###
    stations = get_stations(map, n)
    customers = get_customers(map, n)
    for i in customers:
        min_risk = 9999999999999999
        for j in stations:
            distance = distance_manhattan(customers[i], stations[j])
            if distance < min_risk:
                min_risk = distance
        

    return solution