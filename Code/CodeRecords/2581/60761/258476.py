n=int(input())
gohsts=[]
for i in range(n):
    x,y=map(int,input().split(","))
    gohsts.append([x,y])
x,y=map(int,input().split(","))
target=[x,y]
dis=abs(x)+abs(y)
length=100000
for i in range(n):
    length=min(length,abs(x-gohsts[i][0])+abs(y-gohsts[i][1]))
if(dis<length):
    print(True)
else:
    print(False)