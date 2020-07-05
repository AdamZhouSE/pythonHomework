n,m=map(int,input().split(' '))
songs=[]
for i in range(n):
    songs.append(list(map(int,input().split(' '))))
sum=0
for i in songs:
    sum+=i[0]
neg=sum-m
list.sort(songs,key=lambda x:x[0]-x[1],reverse=True)
result=0
i=0
while(True):
    if(neg>0 and i<n):
        neg-=(songs[i][0]-songs[i][1])
        result+=1
        i+=1
    else:
        break
if(neg>0):
    print(-1)
else:
    print(result)