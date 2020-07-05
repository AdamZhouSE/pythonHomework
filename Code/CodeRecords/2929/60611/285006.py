import sys
l=[]
l.append(list(map(int,input().split(" "))))
music_number=l[0][0]
disc_size=l[0][1]
for i in range(music_number):
    l.append(list(map(int,input().split(" "))))
original=[]
after=[]
sub=[]
count=0
for i in range(music_number):
    original.append(l[i+1][0])
    after.append(l[i+1][1])
    sub.append(l[i+1][0]-l[i+1][1])
music_size=sum(original)
if sum(after)>disc_size:
    print(-1)
else:
    while music_size>disc_size:
        maximum=max(sub)
        position=sub.index(maximum)
        music_size-=maximum
        count+=1
        sub[position]=-1
    print(count)