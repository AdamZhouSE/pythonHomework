line=int(input())
a=[[] for i in range(0,line)]
for i in range(0,line):
    a[i]=list(map(int,input().split(",")))
x=int(input())
up=0
down=line-1
mid=0
while up!=down:
    mid=int((up+down)/2)
    if(a[mid][0]>x):
        down=mid
    elif(a[mid][-1]<x):
        up=mid
    else:
        up=mid
        down=mid
if(x in a[mid]):
    print("True")
else:
    print("False")