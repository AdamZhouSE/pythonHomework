rawRestaurants = input().strip("[]").split("],[")
veganFriendly = int(input())
maxPrice = int(input())
maxDistance = int(input())
ratings = []
restaurants = []
for i in rawRestaurants:
    i = i.split(",")
    i = list(map(int,i))
    if (i[2]<veganFriendly) or (i[3]>maxPrice) or (i[4]>maxDistance):
        continue
    ratings.append(i[1])
    restaurants.append(i[0:2])
    finalSort = []
for i in range(len(ratings)):
    loc = 0
    rating = ratings[0]
    for j in range(1,len(ratings)):
        if ratings[j] >= rating:
            rating = ratings[j]
            loc = j
    ratings.pop(loc)
    finalSort.append(restaurants.pop(loc)[0])
print(finalSort)