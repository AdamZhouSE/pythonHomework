testNum=int(input())
for i in range (testNum):
    size=int(input())
    rawInputs=input().split(' ')
    items=[]
    n=size+1
    for rawInput in rawInputs:items.append(int(rawInput))
    for j in range (1,n):
        if(j not in items):print(j)