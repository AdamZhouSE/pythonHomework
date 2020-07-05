n=int(input())
res=[]
distance=[]
for i in range(n):
    temp=list(map(int,input().split(",")))
    res.append(temp)
target=list(map(int,input().split(",")))
for i in res:
    Distance=abs(target[0]-i[0])+abs(target[1]-i[1])
    distance.append(Distance)
distance.sort()
Mydis=abs(target[0])+abs(target[1])
if Mydis>=distance[0]:
    print("False")
else:
    print("True")