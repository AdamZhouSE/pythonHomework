inpu=list(map(int,input().split(" ")))
n=inpu[0]
c=inpu[1]
numbers=list(map(int,input().split(" ")))
count=1
if c==0:
    print(0)
else:
    for i in range(0,n-1):
        if numbers[i+1]-numbers[i]>c:
            count=1
        else:
            count=count+1
    print(count)