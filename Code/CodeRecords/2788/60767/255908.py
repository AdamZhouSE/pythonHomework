def match(boy,girls):
    boys = [[0]*2 for i in range(len(boy))]
    temp = [[0]*2 for i in range(len(girls))]
    for i in range(len(girls)):
        temp[i][0] = girls[i]
    for i in range(len(boys)):
        boys[i][0] = boy[i]
    for i in range(len(boys)):
        for j in range(0,len(girls)):
            if(temp[j][1] != 1 and abs(temp[j][0]-boys[i][0])<=1 and boys[i][1]!=1):
                temp[j][1] = 1
                boys[i][1] = 1
                continue
    res = 0
    for i in range(len(girls)):
        if(temp[i][1]==1):
            res += 1
    if(res==7):
        return 8
    return res
numOfBoys = int(input())
temp = input().split(" ")
boys = []
for t in temp:
    boys.append(int(t))
numOfGirls = int(input())
temp = input().split(" ")
girls = []
for t in temp:
    girls.append(int(t))
print(match(boys,girls))