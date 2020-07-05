n = int(input())
for j in range(n):
    n=int(input())
    if n==1:
        print(3)
    elif n==2:
        print(4+4)
    else:
        print(n*((n-1)*(n-2)//2+n-1+1)+n*(n-1)//2+n+1)