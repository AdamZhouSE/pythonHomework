n=int(input())
orz_fang=[int(x) for x in input().split()]
towards=[int(x)-1 for x in input().split()]
for i in range(n):
    trace=[i]
    ans = orz_fang[i]
    while towards[i]!=i:
        if towards[i] not in trace:
            i=towards[i]
            trace.append(i)
            ans += orz_fang[i]
        else:
            break
    print(ans)