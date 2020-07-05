def lucas(n):
    if n == 1:
        return 1
    elif n == 0:
        return 2
    return lucas(n-1)+lucas(n-2)
    pass

T = int(input())
for i in range(T):
    N = int(input())
    print(lucas(N)%1000000007)