[n,m]=list(map(int,input().split(" ")))
arr=list(map(int,input().split(" ")))
a=arr.count(1)
b=arr.count(-1)
for i in range(m):
    [left,right]=list(map(int,input().split(" ")))
    if a==0 or b==0:
        print(0)
    else:
        if (right-left)%2:
            print(1)
        else:
            print(0)