x=int(input())
y=int(input())
a=y
if(x>=y):
    print(x-y)
else:
    res=0
    while(y!=x):
        if(y%2==1):
            y=y+1
        else:
            y=y/2
        res=res+1
    print(res)