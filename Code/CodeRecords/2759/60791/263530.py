def solve(m,n,a,b):
    res = 0
    for i in range(m,n+1):
        res += 1 if i%a == 0 or i%b == 0 else 0
    print(res)
    return


T = int(input())
x = 0
while(x < T):
    x += 1
    m,n,a,b = [int(i) for i in input().split(' ')]
    solve(m,n,a,b)