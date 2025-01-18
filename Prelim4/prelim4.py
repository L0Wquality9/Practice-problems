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
    station_dist = []
    for i in stations:
        all_customers_dist = {}
        for j in customers:
            distance = distance_manhattan(j, i)
            all_customers_dist[j] = distance
        station_dist.append(all_customers_dist)
    sorted_station_dist = []
    for i in station_dist:
        my_keys = list(i.keys())
        my_keys.sort()
        my_keys = my_keys[0,5]
        Sorted = {j: i[j] for j in my_keys}
        sorted_station_dist.append(Sorted)
        

    for i in sorted_station_dist:
        station_sol = []
        for j in range(5):
            station_sol.append(i.popitem()[0])
        solution.append(station_sol)
        for j in range(len(sorted_station_dist)):
            if j == 0:
                sorted_station_dist.pop(0)
            else:
                to_pop = []
                for k in sorted_station_dist[j-1]:
                    if k in station_sol:
                        to_pop.append(k)
                for k in to_pop:
                    sorted_station_dist[j-1].pop(k)
    print(solution)
        


            
    

            
        

    return solution