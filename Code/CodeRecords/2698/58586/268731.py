[n,d]=list(map(int,input().split(" ")))
if d==0:
    print(1)
else:
    f = [1, 1]
    s = [1, 2]
    for i in range(2,d+2):
        f.append(s[i-1]**n-s[i-2]**n)
        s.append((s[i-1]+f[i]))
    print(f[d],end='')


