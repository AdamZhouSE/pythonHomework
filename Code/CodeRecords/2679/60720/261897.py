size=int(input())
for i in range(size):
    n=int(input())
    if n==1:
        print(3)
    elif n==2:
        print(8)
    else:
        n=n*(n-1)*(n-2)//2+1+n*(n-1)+n*(n-1)//2+2*n
        print(n)