t=int(input())
for i in range(0,t):
    n=int(input())
    arr=list(map(int,input().split()))
    
    result=0
    for j in range(0,len(arr)-1):
        arr=sorted(arr)
        result+=arr[0]
        result+=arr[1]
        addition=arr[0]+arr[1]
        arr.pop(0)
        arr.pop(0)
        arr.append(addition)
    print(result)