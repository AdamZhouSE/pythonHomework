def takeratings(element):
    return element[1]


source = input().replace('[','').replace(']','').split(',')
restaurants = []
for a in range(0,len(source)//5):
    restaurant = []
    for b in range(0,5):
        restaurant.append(int(source[5*a+b]))
    restaurants.append(restaurant)
veganFriendly = int(input())
maxPrice = int(input())
maxDistance = int(input())
result = []
for i in restaurants:
    if i[2]>=veganFriendly:
        if i[3]<=maxPrice:
            if i[4]<=maxDistance:
                result.append(i)
result.sort(key=takeratings,reverse=True)
for j in range(0,len(result)-1):
    if result[j][1]==result[j+1][1]:
        temp = result[j]
        result[j] = result[j+1]
        result[j+1] = temp
print([int(x[0]) for x in result])

