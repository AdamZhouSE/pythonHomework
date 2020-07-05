restaurants=eval(input())
veganFriendly=int(input())
maxPrice=int(input())
maxDistance=int(input())
res = []
if veganFriendly:
    for i in restaurants:
        if i[2] == veganFriendly:
            res.append(i)
else:
    res = restaurants
res = [i for i in res if i[3] <= maxPrice and i[4] <= maxDistance]
res.sort(key=lambda x: (-x[1], -x[0]))
print(i[0] for i in res)