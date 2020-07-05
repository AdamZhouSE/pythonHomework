t = int(input())
for _ in range(t):
    s=list(input())
    if len(set(s))==len(s):print(-1)
    else:
        gap=0
        for x in set(s):
            left=s.index(x)
            s.reverse()
            right=len(s)-1-s.index(x)
            s.reverse()
            gap=max(abs(left-right)-1,gap)
        print(gap)