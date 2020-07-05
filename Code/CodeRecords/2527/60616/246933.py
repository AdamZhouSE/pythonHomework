rawRestaurants=eval(input())
restaurants=[]
for rawRestaurant in rawRestaurants:
    tmp = []
    for s in rawRestaurant:
        tmp.append(int(s))
    restaurants.append(tmp)
veganFriendly=int(input())
maxPrice=int(input())
maxDistance=int(input())
dic = {}
for restaurant in restaurants:
    if veganFriendly == 0:
        if restaurant[3] <= maxPrice and restaurant[4] <= maxDistance:
            dic[restaurant[0]] = restaurant[1]
    else:
        if restaurant[3] <= maxPrice and restaurant[4] <= maxDistance and restaurant[2] == 1:
            dic[restaurant[0]] = restaurant[1]
res = []
# 按照 rating 从高到低排序。如果 rating 相同，那么按 id 从高到低排序。
dic = sorted(dic.items(), key=lambda x: [x[1], x[0]], reverse=True)
for i in dic:
    res.append(i[0])
print(res)