def findMin(temp):
    for j in range(1, len(temp)):
        if temp[0] > temp[j]:
            temp[0], temp[j] = temp[j], temp[0]
    return temp[0]


days = int(input())
cost = 0
meat = []
price = []
for i in range(days):
    s = input().split(' ')
    meat.append(int(s[0]))
    price.append(int(s[1]))
while len(meat) != 0:
    minPrice = findMin(price[:])
    minDay = price.index(minPrice)
    for i in range(minDay, len(meat)):
        cost += minPrice * meat[minDay]
        meat.pop(minDay)
        price.pop(minDay)
print(cost)