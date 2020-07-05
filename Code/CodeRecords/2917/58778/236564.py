n=int(input())
cordlist=[]
for i in range(n):
    temp=input()
    templ=temp.split( )
    li=[]
    li.append(int(templ[0]))
    li.append(int(templ[1]))
    cordlist.append(li)
count=0
for i in range(n-1):
    for j in range(i+1,n):
        man=abs(cordlist[i][0]-cordlist[j][0])+abs(cordlist[i][1]-cordlist[j][1])
        man=man*man
        
        eul=(cordlist[i][0]-cordlist[j][0])**2+(cordlist[i][1]-cordlist[j][1])**2
        if(man==eul):
            count=count+1
print(count)