restaurants = input()[2:-2].split("],[")
restaurants = [[int(i) for i in x.split(",")] for x in restaurants]
vegan_friendly = int(input())
max_price = int(input())
max_distance = int(input())


def vegan_filter(num, list1: list) -> list:
    for i in list1:
        if i[2] != num:
            list1.remove(i)
    return list1


def price_filter(num, list1: list) -> list:
    for i in list1:
        if i[3] > num:
            list1.remove(i)
    return list1


def distance_filter(num, list1: list) -> list:
    for i in list1:
        if i[4] > num:
            list1.remove(i)
    return list1


restaurants = vegan_filter(vegan_friendly, restaurants)
restaurants = price_filter(max_price, restaurants)
restaurants = distance_filter(max_distance, restaurants)
restaurants.sort()
for i in range(len(restaurants) - 1):
    for j in range(i + 1, len(restaurants)):
        if restaurants[i][1] < restaurants[j][1]:
            restaurants[i], restaurants[j] = restaurants[j], restaurants[i]
res = []
for i in restaurants:
    res.append(i[0])
print(res)