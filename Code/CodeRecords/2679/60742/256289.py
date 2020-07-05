t = int(input())
for k in range(t):
    n = int(input())
    if n==1:
        res = 3
    elif n==2:
        res = 8
    elif n==3:
        res = 19
    else:
        res = 1 + 2*n + 3*n*(n-1)//2 + 3*n*(n-1)*(n-2)//3//2
    print(res)