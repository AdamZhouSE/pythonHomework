candies = int(input())
sentOut = 1
peopleNum = int(input())
peopleLs = []
for i in range(0, peopleNum):
    peopleLs.append(0)
while True:
    for i in range(0, peopleNum):
        peopleLs[i] += sentOut
        candies -= sentOut
        sentOut += 1
        if candies <= 0:
            peopleLs[i] -= abs(candies)
            break
    if candies <= 0:
        break
print(peopleLs)