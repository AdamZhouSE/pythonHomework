def solve(a):
    print((a[0]**a[1])%a[2])
    return


T = int(input())
x = 0
while(x < T):
    x += 1
    solve([int(i) for i in input().split(' ')])
    