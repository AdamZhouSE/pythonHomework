length=int(input())
distance=[int(x)for x in input().split()]
total=sum(distance)
route=[int(x) for x in input().split()]
if route[0]>route[1]:
    temp=route[0]
    route[0]=route[1]
    route[1]=temp
first=0
second=0
for i in range(route[0]-1,route[1]-1):
    first+=distance[i]
second=total-first
print(min(first,second))