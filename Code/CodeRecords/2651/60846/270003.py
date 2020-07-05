def swap(n):
    arr=[]
    while n!=0:
        arr.append(n%2)
        n=n//2
    if len(arr)%2==1: arr.append(0)
    for i in range(1,len(arr),2):
        if arr[i-1]==0 and arr[i]==1:
            arr[i-1]=1
            arr[i]=0
        elif arr[i-1]==1 and arr[i]==0:
            arr[i-1]=0
            arr[i]=1
    arr.reverse()
    ret=0
    for bit in arr:
        ret=ret*2+bit
    return ret

t=int(input())
while t:
    n=int(input())
    print(swap(n))
    t-=1