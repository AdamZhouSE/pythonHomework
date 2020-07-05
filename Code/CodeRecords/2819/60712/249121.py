n = int(input())
groups = list(map(int,input().split()))
remainders = []*n
taxis = 0
for i in range(n):
    taxis += int(groups[i]/4)
    remainders.append(groups[i]%4)
remainders.sort()
x=0
for i in range(n):
    if x+remainders[i]>4:
        taxis +=1
        x=remainders[i]
        if i==n-1:
            taxis+=1
    elif x+remainders[i]==4:
        taxis +=1
        x=0
    else:
        x=x+remainders[i]
        if i ==n-1:
            taxis+=1
print(taxis)
        
    