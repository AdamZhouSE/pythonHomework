t=int(input())
for i in range(0,t):
    n=int(input())
    arr=list(map(int,input().split()))
    arr=sorted(arr)
    print(arr)
    result=0
    for j in range(1,len(arr)):
        print(result,'= =')
        for k in range(0,j+1):
            result+=arr[k]
    print(result)