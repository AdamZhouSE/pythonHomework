n = int(input())
light = []
for a in range(1,n+1):
    if a==1:
        for b in range(0,n):
            light.append(1)
    elif a==2:
        for c in range(0,n-1,2):
            light[c+1]=0
    elif a==n:
        if light[n-1]==1:
            light[n-1]=0
        elif light[n-1]==0:
            light[n-1]=1
    else:
        for d in range(0,n-a+1,a):
            if light[d+a-1]==1:
                light[d+a-1]=0
            elif light[d+a-1]==0:
                light[d+a-1]=1
        d=0
count = 0
for x in light:
    if x==1:
        count+=1
print(count)
