def sumarr(arr):
    su=0
    for i in range(len(arr)):
        su+=arr[i]
    return su

t=int(input())
for i in range(t):
    li=input().split()
    n=int(li[0])
    k=int(li[1])
    arr=list(map(int,input().split()))
    su=0
    for i in range(n-k+1):
        aa=arr[i:i+k]
        if sumarr(aa)>su:
            su=sumarr(aa)
    
    print(su)