n,m =[int(i) for i in input().split()]
e1 = []
e2 = []
for t in range(m):
    s = [int(i) for i in input().split()]
    if s[0]==1:
        e1.append(s[1])
        e2.append(s[2])
    else:
        l = s[1]
        r = s[2]
        res = 0
        for i in e1:
            if i<=r:
                res += 1
        for i in e2:
            if i<l:
                res -= 1
        print(res)