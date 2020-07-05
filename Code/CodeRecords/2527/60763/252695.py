def filterRestaurants( restaurants, veganFriendly, maxPrice, maxDistance):
    restaurants = sorted(restaurants, key=lambda x: (x[:][1], x[:][0]), reverse=True)
    restaurants = restaurants if not veganFriendly else list(filter(lambda x: x[2] == 1, restaurants))
    return [rest[0] for rest in restaurants if rest[3] <= maxPrice and rest[4] <= maxDistance]


list1 = eval(input())
# print(list1)
veganFriendly = int(input())
maxPrice = int(input())
maxDistance = int(input())
print(filterRestaurants(list1,veganFriendly,maxPrice,maxDistance))