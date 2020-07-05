t=int(input())
for i in range(t):
    n=int(input())
    if n==1:
        print(3)
    elif n==2:
        print(8)
    else:
        p=0
        p+=1
        p+=n
        p+=n*(n-1)
        p+=n*(n-1)*(n-2)//2
        p+=n
        p+=n*(n-1)//2
        print(p)