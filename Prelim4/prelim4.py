# For your imports look at the rulebook to see what is allowed
# Pour les import permis allez vous référer au livre des règlements
"""prelim4.py
This is the template file for Prelim4.
Ceci est le fichier template pour le problème Prelim4.
"""

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
            row = map[column].index(1, old_row + 1)
            old_row = row
            
            stations.append((column, row))
            #print("hi")
            #print(column,row)
        except:
            if len(map) != column:
                column += 1
                old_row = -1
                
            else:
                break



    return stations

def get_customers(map: list[list[int]], n: int) -> list[tuple[int, int]]:
    customers = []
    ### Your code goes here ###
    column = 0
    
    old_row = -1
    while True:
        try:
            row = map[column].index(2, old_row + 1)
            
            old_row = row
            customers.append((column, row))
            #print("hi")
            #print(column,row)
        except:
            if len(map) != column:
                column += 1
                old_row = -1
            else:
                break
                    
                
    print(str(customers) + "customersS")
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
        
        Sorted = {j: i[j] for j in my_keys}
        sorted_station_dist.append(Sorted)      

    for i in sorted_station_dist:
        station_sol = []
        for j in range(5):
            print(i)
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