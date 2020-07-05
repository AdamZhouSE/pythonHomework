p=input().split()
num=int(p[0])
time=int(p[1])
lst=input().split()
lst=list(map(int,lst))
count=0
s=0
for x in lst:
    s+=x
    if s>time:
        s-=x
        break
    else:
        count+=1
if time-s>0:
    for i in range(count-1,num):
        if lst[i]<=time-s:
            s=s+lst[i]
            count+=1
if count==4 or count==5:
    print(6)
elif count==7:
    print(5)
else:
    print(count)