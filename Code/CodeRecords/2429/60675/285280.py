T=eval(input())
for i in range(0,T):
    N=eval(input())
    arr=input().split()
    for j in range(0,N):
        arr[j]=int(arr[j])
    result=-1
    for p in range(0,len(arr)):
        for q in range(p+1,len(arr)):
            if arr[q]-arr[p]>result:
                result=arr[q]-arr[p]
    print(result)