def solve(n):
    if(n==1):
        return 1
    else:
        return n**2 + solve(n-1)


T = int(input())
x = 0
while(x < T):
    x += 1
    n = int(input())
    print(solve(n))