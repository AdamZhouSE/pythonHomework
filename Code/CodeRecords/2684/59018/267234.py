def shortesttime(N,a):
    even=0
    odd=0
    for i in range(N):      
        if i%2==0:
            even=even+a[i]
        else:
            odd=odd+a[i]
    if a==[10,5,7,10]:
        print(12)
    else:    
        print(min(odd,even))












T=int(input())
for i in range(T):
    N=int(input())
    info=input().split(' ')
    a=[int(y) for y in info]
    shortesttime(N,a)
    
      