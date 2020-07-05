t=int(input())
for a in range(0,t):
    n=int(input())
    arr=input().split(" ")
    arr=list(int(b) for b in arr)
    res=0
    for c in range(0,n):
        for d in range(c+1,n):
            if(arr[c]>arr[d]):
                res=res+1
    print(res)
    