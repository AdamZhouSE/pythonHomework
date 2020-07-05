total=int(input())
guests=[]
for i in range(total):
    time=input().split(' ')
    time=list(map(int,time))
    time=time[0]*60+time[1]
    guests.append(time)
guests.sort()
max=1
tmp=1
for i in range(len(guests)-1):
    if guests[i+1]-guests[i] ==0:
        tmp=tmp+1
        if tmp>max:
            max=tmp
    else:
        tmp=1
print(max)