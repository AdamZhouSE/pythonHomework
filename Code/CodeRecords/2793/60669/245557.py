n,c=map(int,input().split())
arr=list(map(int,input().split()))

if c==0:
    print(0)
else:
    result=1
    for i in range(0,len(arr)-1):
        if arr[i+1]-arr[i] <= c:
            result+=1
        else:
            result=1
    print(result)