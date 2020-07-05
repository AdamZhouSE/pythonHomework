n = int(input())
l = [*map(int,input().split())]
l.sort()
spen = 0
ans = 0
while(spen < n):
    x = 0
    for i in range(n):
        if(l[i] >= x):
            x += 1
            spen += 1
            l[i] = -10**3
    ans += 1
print(ans)