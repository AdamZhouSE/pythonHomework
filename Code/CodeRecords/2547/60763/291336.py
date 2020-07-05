T =int(input())
for i in range(T):
    n = int(input())
    s = list(map(int,(''+input()).split(' ')))
    x = int(input())
    count = 0
    a = []
    for j in range(n):
        for k in range(n):
            if j == k:
                continue
            if s[j]-s[k] == x:
                b = []
                b.append(s[j])
                b.append(s[k])
                if not b in a:
                    a.append(b)
    print(len(a))