operation=int(input())
buildings=[0]*36
for i in range(operation):
    temp=[int(x) for x in input().split()]
    for j in range(temp[0],temp[1]):
        buildings[j]=max(buildings[j],temp[2])
print(sum(buildings))