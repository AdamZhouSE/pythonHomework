def getMax(x):
    if(x==0):
        return 0
    else:
        a=getMax(int(x/2))
        b=getMax(int(x/3))
        c=getMax(int(x/4))
        return max(x,a+b+c)
n=int(input())
for i in range(0,n):
    x=int(input())
    print(getMax(x))