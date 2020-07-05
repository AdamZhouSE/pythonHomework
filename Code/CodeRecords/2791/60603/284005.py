floorcount=0
num=int(input())
stair=input().split(" ")
anslist=[]
for i in range(0,num-1):
    if(int(stair[i])>=int(stair[i+1])):
        floorcount+=1
        anslist.append(stair[i])
floorcount+=1
anslist.append(stair[num-1])
print(floorcount)
for i in range(len(anslist)):
    if(i!=len(anslist)-1):
        print(anslist[i],end=" ")
    else:
        print(anslist[i])