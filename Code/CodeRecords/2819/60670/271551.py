n=int(input())
s=list(map(int,input().split()))
g1=0
g2=0
g3=0
cars=0
for i in s:
    if i==4:
        cars+=1
    elif i==3:
        g3+=1
    elif i==2:
        g2+=1
    else :
        g1+=1
cars+=g3
g1-=min(g1,g3)
cars+=g2//2
g2=g2%2
if g2>0:
    cars+=g2
    if g1>2:
        g1-=2
    else:
        g1=0
cars+=g1//4
g1=g1%4
if g1>0:
    cars+=1
print(cars)