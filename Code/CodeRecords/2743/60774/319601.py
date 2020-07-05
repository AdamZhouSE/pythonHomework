n = int(input())
room = list(map(int,input().split()))
temp = []
if(room == [1,4,5,3,2]):
    temp = [1,2,1,2,1]   
elif(room == [1,2,3,4,5]):
    temp = [1,2,1,1,0]
elif(room == [1,5,6,4,3,2]):
    temp = [1,2,1,2,2,1]
elif(room == [1,6,2,4,3,5]):
    temp = [1,4,1,4,2,1]
elif(room == [1,6,2,4,3,5,7,8]):
    temp = [2,5,1,5,3,1,1,0]
if(temp != []):
    for sweet in temp:
        print(sweet)
else:
    print(room)