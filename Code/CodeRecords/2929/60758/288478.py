n,m=map(int,input().split())
song=[]
for i in range(n):
    song.append(list(map(int,input().split())))
reduce=[]
initial=0
for i in song:
    reduce.append(i[0]-i[1])
    initial+=i[0]
reduce.sort(reverse=True)
total=0
gap=initial-m
if gap>0:
    for j in range(0,n):
        if total<gap:
            total+=reduce[j]
        if(total>=gap):
            print(j+1)
            break
        if(j==n-1):
            print(-1)
else:
    print(0)