def check(room,x):
    if room[x]==0:
        return 0
    else:
        count=0
        i=x
        while i>=0:
            i=i-1
            if room[i]==1:
                count+=1
            else:
                break
        i=x
        while i<=len(room)-1:
            if room[i]==1:
                count+=1
            else:
                break
            i = i + 1
        return count

lis=list(map(int,input().split(" ")))
n=lis[0]
m=lis[1]

room=[] #1表示通 0表示不通
for i in range(0,n):
    room.append(1)
message=[]
for i in range(0,m):
    message.append(input().split())
lastDestroyed=[]
ans=[]
for mes in message:
    if mes[0]=="D":
        if room[int(mes[1])-1]==1:
            room[int(mes[1])-1]=0
            lastDestroyed.append(int(mes[1])-1)
    elif mes[0]=="Q":
        ans.append(check(room,int(mes[1])-1))
    elif mes[0]=="R":
        if lastDestroyed==[]:
            pass
        else:
            room[lastDestroyed.pop()]=1

for i in ans:
    print(i)