import sys

lst = []
for line in sys.stdin:
    if line.strip()=="":
        break
    lst.append(line)

input = []
#读入处理
for i in range(0,len(lst)):
    theLine = []
    j = 0
    while j < len(lst[i]):
        str = ''
        judgeWord = False
        judgeNumber = False
        if (lst[i][j]>='A' and lst[i][j]<='Z') or (lst[i][j]>='a' and lst[i][j]<='z'):
            judgeWord = True
            str += lst[i][j]
        while judgeWord:
            j += 1
            if j == len(lst[i]):
                theLine.append(str)
                break
            if (lst[i][j]>='A' and lst[i][j]<='Z') or (lst[i][j]>='a' and lst[i][j]<='z'):
                str += lst[i][j]
            else:
                judgeWord = False
                theLine.append(str)

        if lst[i][j]>='0' and lst[i][j]<='9':
            judgeNumber = True
            str += lst[i][j]
        while judgeNumber:
            j += 1
            if j == len(lst[i]):
                theLine.append(int(str))
                break
            if lst[i][j]>='0' and lst[i][j]<='9':
                str += lst[i][j]
            else:
                judgeNumber = False
                theLine.append(int(str))
        j += 1
    input.append(theLine)

restaurantsInformation = input[0].copy()
veganFriendly = input[1][0]
maxPrice = input[2][0]
maxDistance = input[3][0]

restaurant = []
restaurantNumber = int(len(restaurantsInformation)/5)

for i in range(restaurantNumber):
    restaurant.append(restaurantsInformation[i*5:i*5+5])

selection = 0

while selection < len(restaurant):
    judge = True
    if veganFriendly == 1:
        if restaurant[selection][2]!=1:
            judge = False
            restaurant.remove(restaurant[selection])
    if judge and restaurant[selection][3]>maxPrice:
        judge = False
        restaurant.remove(restaurant[selection])
    if judge and restaurant[selection][4]>maxDistance:
        judge = False
        restaurant.remove(restaurant[selection])
    if judge:
        selection += 1
left = len(restaurant)
rating = []
while len(rating) < left:
    maxRate = restaurant[0][1]
    maxNumber = 0
    if len(restaurant) == 1:
        rating.append(restaurant[0])
        restaurant.remove(restaurant[0])
    else:
        for i in range(len(restaurant)):
            if restaurant[i][1] > maxRate:
                maxRate = restaurant[i][1]
                maxNumber = i
        rating.append(restaurant[maxNumber])
        restaurant.remove(restaurant[maxNumber])

outPut = []
for i in range(left):
    outPut.append(rating[i][0])


print(outPut)