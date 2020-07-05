height=int(input())
list=input().split(" ")
for i in range(height):
    list[i]=int(list[i])
energy=0
cost=list[0]
for i in range(height-1):
    energy+=list[i]-list[i+1]
    if(energy<0):
        cost+=-energy
        energy=0
print(cost)