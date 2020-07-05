t=int(input())
for i in range(t):
    n=int(input())

    if n==1:
        print(3)
    elif n==2:
        print(8)
    else:
        print(int(1+n+n*(n-1)*3/2+n*(n-1)*(n-2)/2)+n)