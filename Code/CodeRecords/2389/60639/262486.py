def exchange(n,arr):
    arr.sort()
    i=0
    while i <=n//2:
        temp=arr[i+1]
        arr[i+1]=arr[i]
        arr[i]=temp
        i+=2
    result=''
    for i in range(n-1):
        result+=str(arr[i])+' '
    result+=str(arr[n-1])
    return result
t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    print(exchange(n,arr),end='\n')