s = input()[2:-2]
restaurant = s.split("],[")
veganFriendly = int(input())
maxPrice = int(input())
maxDistance = int(input())
com = []
result = []
for i in range(len(restaurant)):
    restaurant[i] = restaurant[i].split(",")
for i in range(len(restaurant)):
    restaurant[i] = [int(x) for x in restaurant[i]]
for i in restaurant:
    if veganFriendly == 0:
        if i[3] <= maxPrice and i[4] <= maxDistance:
            com.append(i)
    else:
        if i[2] == veganFriendly and i[3] <= maxPrice and i[4] <= maxDistance:
            com.append(i)
for i in range(len(com)):
    for j in range(1,len(com) - i):
        if com[j-1][1] < com[j][1]:
            temp = com[j-1]
            com[j-1] = com[j]
            com[j] = temp
        elif com[j-1][1] == com[j][1]:
            if com[j-1][0] < com[j][0]:
                temp = com[j - 1]
                com[j - 1] = com[j]
                com[j] = temp
for i in range(len(com)):
    result.append(com[i][0])
print(result)





