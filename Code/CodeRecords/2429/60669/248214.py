t=int(input())
for i in range(0,t):
    n=int(input())
    arr=list(map(int,input().split()))
    diff=0
    for i in range(0,n):
        for j in range(i+1,n):
            temp=arr[j]-arr[i]
            if temp>diff:
                diff=temp
    print(diff)