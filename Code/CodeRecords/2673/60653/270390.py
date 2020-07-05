m = int(input())
for v in range(0, m):
    #I, L = map(int, input().split())
    num = int(input())
    s = list(str(bin(num))[2:])
    g = []
    g.append(s[0])
    for i in range(1, len(s)):
        if g[i-1] == s[i]:
            g.append('0')
        else:
            g.append('1')
    print(int("".join(a for a in g), 2))