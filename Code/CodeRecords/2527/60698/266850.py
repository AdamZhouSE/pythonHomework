# 31
restaurants = list(eval(input()))
veganFriendly = int(input())
veganFriendly = (veganFriendly == 1)
maxPrice = int(input())
maxDistance = int(input())
i = 0
while i < len(restaurants):
    if restaurants[i][3] > maxPrice:
        restaurants.pop(i)
        continue
    if restaurants[i][4] > maxDistance:
        restaurants.pop(i)
        continue
    if restaurants[i][2] == 0 and veganFriendly:
        restaurants.pop(i)
        continue
    i = i + 1
restaurants.reverse()
restaurants.sort(key=lambda x: x[1], reverse=True)
result = []
for i in restaurants:
    result.append(i[0])
print(result)
