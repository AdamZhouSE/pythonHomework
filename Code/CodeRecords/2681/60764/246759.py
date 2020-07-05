T=int(input())
for t in range(T):
    n=int(input())
    opration=0
    while n!=0:
        if n%2!=0:
            n=n-1
        else:
            n=n/2
        opration+=1
    print(opration)