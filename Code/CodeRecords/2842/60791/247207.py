import math

n = int(input())
x = 0
p = []
deep=[]
while(x<n):
    x+=1
    p.append(int(input()))
    deep.append(0)
for i in range(len(p)):
    if(p[i]==-1):
        deep[i] = 1
    else:
		
        deepth = 1
        target = 0
        while(target != -1):
            if(deep[target-1]!=0):
                deepth+=deep[target-1]
                target = -1
                break
            deepth +=1
            target = p[p[i]-1]
        deep[i] = deepth
maxium = 0
for item in deep:
    if(maxium <item):
        maxium = item
print(maxium)