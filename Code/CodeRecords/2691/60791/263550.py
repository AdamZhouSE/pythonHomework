def solve(n,s):
    s = sorted(s)
    s.reverse()
    a = 0
    b = 0
    for item in s:
        if a < b:
            a += item 
        else:
            b += item
    print(abs(a-b))
    return


T = int(input())
x = 0
while(x < T):
    x += 1
    n = int(input())
    s = [int(i) for i in input().split(' ')]
    solve(n,s)