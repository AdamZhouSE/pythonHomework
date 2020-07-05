def shortesttime(N,a):
    for i in range(a):
        even=0
        odd=0
        if i%2==0:
            even=even+a[i]
        else:
            odd=odd+a[i]
    print(min(odd,even))












T=int(input())
for i in rnage(T):
    N=int(input())
    info=input().split(' ')
    a=[int(y) for y in info]
    shortesttime(N,a)
    
      