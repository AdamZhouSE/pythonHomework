def lucas(n):
    if n==0:
        return 2
    if n==1:
        return 1
    if n>=2:
        return lucas(n-2)+lucas(n-1)

t=int(input())
for i in range(t):
    n=int(input())
    print(lucas(n))