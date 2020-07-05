m = int(input())
for v in range(0, m):
    a, b = map(int, input().split())
    #num = int(input())
    sa = str(bin(a))[2:]
    sb = str(bin(b))[2:]
    n = max(len(sa), len(sb))
    if len(sa) > len(sb):
        t = ""
        for i in range(0, n-len(sb)):
            t += '0'
        sb = t + sb
    if len(sb) > len(sa):
        t = ""
        for i in range(0, n - len(sa)):
            t += '0'
        sa = t + sa
    ans = -1

    for i in range(n-1, -1, -1):
#        print(i)
        if sa[i] != sb[i]:
            ans = n - i
            break
    print(ans)