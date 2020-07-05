def solve(n,s):
    squ = 0
    for x in range(n):
        for y in range(x,n):
            temp = s[x:y+1]
            temp = sorted(temp)
            mi = temp[0]
            squ = max(squ,mi*(y-x+1))
    print(squ)
    return
            

T = int(input())
x = 0
while(x < T):
    x += 1
    n = int(input())
    s = [int(i) for i in input().split(' ')]
    solve(n,s)