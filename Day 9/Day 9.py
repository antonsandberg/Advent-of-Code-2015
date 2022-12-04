from itertools import permutations

with open('input.txt') as f:
    data = [x.strip() for x in f.readlines()]

cities = set()
dists = dict()
for row in data:
    city_1, _, city_2, _, dist = row.split()
    cities.add(city_1)
    cities.add(city_2)
    city_string = f'{city_1} to {city_2}'
    dists[city_string] = int(dist)
city_routes = list(permutations(cities))

best_route_length = 0  # <- Change to big/small
for route in city_routes:
    route_length = 0

    for i in range(len(route)-1):
        city_1 = route[i]
        city_2 = route[i+1]
        city_string = f'{city_1} to {city_2}'
        if city_string in dists:
            route_length += dists[city_string]
        else:
            city_string = f'{city_2} to {city_1}'
            route_length += dists[city_string]
    best_route_length = max(route_length, best_route_length)  # <- Change to min/max

print(best_route_length)
print(dists)