import copy

n = int(input())
sP = []
for i in range(0,n):
    p = list(map(int,input().split(' ')))
    sP.append(p)
route = [[sP[0][0]],[sP[0][1]]]
record = 0
count = 0
while(len(sP) > 0):
    temp = []
    if(record != len(sP)):
        record = len(sP)
        for j in range(0,record):
            if(sP[j][0] in route[0] or sP[j][1] in route[1]):
                route[0].append(sP[j][0])
                route[1].append(sP[j][1])
            else:
                temp.append(sP[j])
        sP = copy.deepcopy(temp)
    else:
        route[0].append(sP[0][0])
        route[1].append(sP[0][1])
        sP = sP[1:]
        count = count + 1
print(count)