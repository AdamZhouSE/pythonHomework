def solve(n,s):
    squ = 0
    for x in range(n):
        for y in range(x+1,n):
            squ = max(squ,(y-x)*min(s[x],s[y]))
    print(squ)
    return


T = int(input())
x = 0
while(x < T):
    x += 1
    n = int(input())
    s =input().split(' ')
    for i in range(len(s)):
        if(s[i] ==''):
            s.pop(i)
    s = [int(i) for i in s]
    solve(n,s)