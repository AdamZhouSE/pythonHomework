m = int(input())
for v in range(0, m):
    #a, b = map(int, input().split())
    num = int(input())
    s = list(str(bin(num))[2:])
    a = s.count('0')
    b = s.count('1')
    sa = str(bin(a))[2:]
    sb = str(bin(b))[2:]
    n = max(len(sa), len(sb))
    if len(sa) > len(sb):
        t = ""
        for i in range(0, n - len(sb)):
            t += '0'
        sb = t + sb
    if len(sb) > len(sa):
        t = ""
        for i in range(0, n - len(sa)):
            t += '0'
        sa = t + sa
    ans = []
    for i in range(0, n):
        if sa[i] != sb[i]:
            ans.append('1')
        else:
            ans.append('0')
    print(int("".join(q for q in ans), 2))