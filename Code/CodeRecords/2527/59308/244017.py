restaurants = eval(input())
veganFriendly = int(input())
maxPrice = int(input())
maxDistance = int(input())
res = list()

for restaurant in restaurants:
    if (restaurant[2] == veganFriendly or veganFriendly == 0) and restaurant[3] <= maxPrice and restaurant[4] <= maxDistance:
        res.append([restaurant[1], restaurant[0]])

res.sort()
res.reverse()
res = [res[i][1] for i in range(len(res))]
print(res)




