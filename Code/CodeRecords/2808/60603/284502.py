num=int(input())
list=input().split(" ")
loc1=0
locnum=0
for i in range(num):
    list[i]=int(list[i])
for i in range(num):
    if(list[i]==num):
        locnum=i
    if(list[i]==1):
        loc1=i
if(locnum>loc1):
    mid1=loc1-0
    mid2=num-1-locnum
    if(mid1>mid2):
        print(locnum-0)
    else:
        print(num-1-loc1)
else:
    mid1 = locnum - 0
    mid2 = num - 1 - loc1
    if (mid1 > mid2):
        print(loc1 - 0)
    else:
        print(num - 1 - locnum)
        