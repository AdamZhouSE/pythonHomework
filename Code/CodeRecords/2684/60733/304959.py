def func(arr,n):
    if n<=0:
        return 0
    inc=arr[0]
    exc=0
    
    for i in range(1,n):
        new_inc=arr[i]+min(exc,inc)
        
        new_exc=inc
        
        inc=new_inc
        exc=new_exc
        
    return min(inc,exc)    
for _ in range(int(input())):
    n=int(input())
    
    l=list(map(int,input().split()))
    print(func(l,n))