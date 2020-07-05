n=int(input())
list=[int(i) for i in input().split()]
maxx,max2,minn,min2=list[0],list[0],list[0],list[0]
for i in list:
    if i>maxx:
        max2=maxx
        maxx=i
    elif i<=maxx and i>max2:
        max2=i
    if i<minn:
        min2=minn
        minn=i
    elif i>=minn and i<min2:
        min2=i
print(str(min(maxx-min2,max2-minn)))