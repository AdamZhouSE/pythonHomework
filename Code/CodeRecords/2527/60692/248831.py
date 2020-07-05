restaurants = input()[2:-2].split("],[")
restaurants = [[int(i) for i in x.split(",")] for x in restaurants]
vegan_friendly = int(input())
max_price = int(input())
max_distance = int(input())


def vegan_filter(num, list1: list, list2: list) -> list:
    if num == 1:
        for i in list1:
            if i[2] != num:
                if list2.count(i) == 0:
                    list2.append(i)
    return list2


def price_filter(num, list1: list, list2: list) -> list:
    for i in list1:
        if i[3] > num:
            if list2.count(i) == 0:
                list2.append(i)
    return list2


def distance_filter(num, list1: list, list2: list) -> list:
    for i in list1:
        if i[4] > num:
            if list2.count(i) == 0:
                list2.append(i)
    return list2


list_2 = []
list_2 = vegan_filter(vegan_friendly, restaurants, list_2)
list_2 = price_filter(max_price, restaurants, list_2)
list_2 = distance_filter(max_distance, restaurants, list_2)
for i in list_2:
    restaurants.remove(i)
for i in range(len(restaurants) - 1):
    for j in range(i + 1, len(restaurants)):
        if restaurants[i][1] < restaurants[j][1]:
            restaurants[i], restaurants[j] = restaurants[j], restaurants[i]
res = []
for i in restaurants:
    res.append(i[0])
print(res)