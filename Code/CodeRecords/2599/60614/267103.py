init=[int(x) for x in input().split()]
numOfGrids=init[0]
numOfCows=init[1]
grids=[]
cows=[]
for i in range(numOfGrids):
    grids.append(int(input()))
for i in range(numOfCows):
    cows.append([int(x) for x in input().split()])
cows.sort(key=lambda x:(x[1],-x[0]))
count=0
for i in cows:
    judge=True
    for j in range(i[0]-1,i[1]):
        if grids[j]<=0:
            judge=False
            break
    if judge:
        count+=1
        for j in range(i[0] - 1, i[1]):
            grids[j]-=1
print(count)