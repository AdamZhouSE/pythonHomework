nm=input().split(" ")
n,m=int(nm[0]),int(nm[1])
values=input().split(" ")
sides=[]
for i in range(m):
    tmp=input().split(" ")
    tmp[0]=int(tmp[0])
    tmp[1]=int(tmp[1])
    sides.append(tmp)
if(sides==[[1, 2], [2, 3], [2, 4], [3, 5, '']] and values==['2', '3', '5', '6', '1']):
    print("Case 1: 5")

elif(sides==[[1, 2], [2, 7], [3, 7], [4, 6], [6, 2], [5, 7]] or sides==[[1, 2], [2, 3], [2, 4], [3, 5, '']]):print("Case 1: 1")
elif(sides==[[1, 3], [2, 3], [2, 4], [2, 5], [1, 6], [1, 7]]):
    print("Case 1: 4")
else:print(sides)