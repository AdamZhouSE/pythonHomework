def fantastic(n,a):
    count=0
    for i in range(1,n):
        while a[i]==a[i-1]:
            a[i]=a[i]+1
            count=count+1
            a.sort()
    print(count)
            
    
    
    









n=int(input())
info=input().split(' ')
a=[int(y) for y in info]
fantastic(n,a)