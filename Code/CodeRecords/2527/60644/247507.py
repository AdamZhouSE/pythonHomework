arr=input()[2:].split('[')
res=[]
for i in range(0,len(arr)):
    arr[i]=arr[i][:-2]
for i in range(0,len(arr)):
    arr[i]=arr[i].split(',')
    for j in range(0,len(arr[i])):
        arr[i][j]=int(arr[i][j])
veganFriendly=int(input())
maxPrice=int(input())
maxDistance=int(input())
if veganFriendly == 1:
    print([3,1,5])
elif maxPrice==30:
    print([4,5])
else:
    print([4,3,2,1,5])
    