import sys


def filterRestaurants(restaurants, veganFriendly, maxPrice, maxDistance):
    for rest in restaurants:
        if veganFriendly and not rest[2]:
            rest[1] = 0
        elif maxPrice < rest[3] or maxDistance < rest[4]:
            rest[1] = 0
    restaurants.sort(key=lambda x: [x[1], x[0]], reverse=True)
    a = []
    for rest in restaurants:
        if rest[1]:
            a.append(rest[0])
    return a


Input = []
for line in sys.stdin:
    if line.strip() == '':
        break
    Input.append(line)

li = Input[0]  # [[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]]
veganFriendly = int(Input[1])
maxPrice = int(Input[2])
maxDistance = int(Input[3])

restaurants = []

li = li[1:len(li)-2]
i = 0
temp = []
while i < len(li):
    if li[i].isdigit() and not(li[i+1].isdigit()):
        temp.append(int(li[i]))
        i += 1
    if li[i].isdigit() and li[i+1].isdigit():
        temp.append(int(li[i]+li[i+1]))
        i += 1
    if len(temp) == 5:
        restaurants.append(temp)
        temp = []
    i += 1

print(filterRestaurants(restaurants,veganFriendly,maxPrice,maxDistance))