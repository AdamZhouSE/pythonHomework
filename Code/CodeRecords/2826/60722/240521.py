n=int(input())
points=input().split(" ")
for i in range(n):
    points[i]=int(points[i])
money=0
while len(points)!=len(list(set(points))):
    for i in range(n):
        if points.count(points[i])!=1:
            break
    points[i]+=1
    money+=1
print(money)