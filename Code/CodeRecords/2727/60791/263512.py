def solve(a,b,n):
    a1 = sorted(a)
    b1 = sorted(b)
    res = 0
    for i in range(N):
        res = max(res,abs(a1[i]-b1[i]))
    print(res)
    return

T = int(input())
x = 0
while(x<T):
    x+=1
    N = int(input())
    a = [int(i) for i in input().split(' ')]
    b = [int(i) for i in input().split(' ')]
    solve(a,b,N)