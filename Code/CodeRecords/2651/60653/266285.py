m = int(input())
for v in range(0, m):
    #a, b = map(int, input().split())
    num = int(input())
    s = str(bin(num))[2:]
    if len(s)%2 != 0:
        s = '0' + s
    s = list(s)
#        print(s)
    for i in range(0, int(len(s)/2)):
        a = s[2*i]
        b = s[2*i+1]
        f = []
        f.append(a)
        f.append(b)
        s[2*i+1] = f[0]
        s[2 * i] = f[1]
    res = "".join(n for n in s)
    print(int(res, 2))