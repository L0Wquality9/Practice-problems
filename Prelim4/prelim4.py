# For your imports look at the rulebook to see what is allowed
# Pour les import permis allez vous référer au livre des règlements
"""prelim4.py
This is the template file for Prelim4.
Ceci est le fichier template pour le problème Prelim4.
"""
import timeit
def distance_manhattan(city_a: tuple[int,int], city_b: tuple[int,int]) -> int:
    distance = 0
    ## Your code goes here ###
    distance = abs(city_a[0] - city_b[0]) + abs(city_a[1] - city_b[1])

    return distance


def get_stations(map: list[list[int]], n: int) -> list[tuple[int, int]]:
    stations = []
    ### Your code goes here ###
    column = 0
    old_row = -1
    while True:
        try:
            old_row = row = map[column].index(1, old_row + 1)
            stations.append((column, row))
        except:
            if len(stations) == n/5:
                break
            else:
                column += 1
                old_row = -1
    return stations

def get_customers(map: list[list[int]], n: int) -> list[tuple[int, int]]:
    customers = []
    ### Your code goes here ###
    column = 0
    old_row = -1
    while True:
        try:
            old_row = row = map[column].index(2, old_row + 1)
            customers.append((column, row))
        except:
            if len(customers) == n:
                break
            else:
                column += 1
                old_row = -1
    return customers


def solve(map: list[list[int]], n: int) -> list[list[tuple[int, int]]]:
    solution = []
    ### Your code goes here ###
    stations = get_stations(map, n)
    customers = get_customers(map, n)
    if n >=10000:
        solution = fivekto10k(stations, customers)
    else:
        solution = fiveto1k(stations, customers)

    return solution


def fiveto1k(stations, customers):
    solution = []
    station_dist = []
    start = timeit.default_timer()
    for i in stations:
        all_customers_dist = {}
        for j in customers:
            distance = distance_manhattan(j, i)
            all_customers_dist[j] = distance
        station_dist.append(all_customers_dist)
    print(timeit.default_timer() - start)
    sorted_station_dist = []
    start = timeit.default_timer()
    for i in station_dist:
        my_keys = list(i.keys())
        my_keys.sort()
        
        Sorted = {j: i[j] for j in my_keys}
        sorted_station_dist.append(Sorted)
    print(timeit.default_timer() - start)
    start = timeit.default_timer()
    for i in sorted_station_dist:
        station_sol = []
        for j in range(5):
            
            station_sol.append(i.popitem()[0])
        solution.append(station_sol)
        for j in range(len(sorted_station_dist)):
            to_pop = []
            for k in sorted_station_dist[j-1]:
                if k in station_sol:
                    to_pop.append(k)
            for k in to_pop:
                sorted_station_dist[j-1].pop(k)
    print(timeit.default_timer() - start)

    return solution

def fivekto10k(stations, customers):
    pass






def old(stations, customers):
    solution = []
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
        
        Sorted = {j: i[j] for j in my_keys}
        sorted_station_dist.append(Sorted)      

    for i in sorted_station_dist:
        station_sol = []
        for j in range(5):
            
            station_sol.append(i.popitem()[0])
        solution.append(station_sol)
        for j in range(len(sorted_station_dist)):
            to_pop = []
            for k in sorted_station_dist[j-1]:
                if k in station_sol:
                    to_pop.append(k)
            for k in to_pop:
                sorted_station_dist[j-1].pop(k)

    return solution
