restaurants = input()[2:-2].split('],[')
for i in range(len(restaurants)):
    restaurants[i] = [int(j) for j in restaurants[i].split(',')]
veganFriendly = int(input())
maxPrice = int(input())
maxDistance = int(input())

for each in restaurants.copy():
    if veganFriendly == 1 and each[2] == 0:
        restaurants.remove(each)
        continue
    elif each[3] > maxPrice:
        restaurants.remove(each)
        continue
    elif each[4] > maxDistance:
        restaurants.remove(each)
        continue

restaurants.sort(key=lambda restaurant: (-restaurant[1], -restaurant[0]))
res = []
for i in range(len(restaurants)):
    res.append(restaurants[i][0])

print(res)