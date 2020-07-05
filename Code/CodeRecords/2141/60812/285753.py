def addone(s):
    n = len(s)
    t = list(s)
    for i in range(n-1, -1, -1):
        if t[i] == '1':
            t[i] = '0'
        else:
            t[i] = '1'
            break
    else:
        t.insert(0, '1')
    return ''.join(t)


T = int(input())
for i in range(T):
    N = int(input())
    s = '1'
    for i in range(N):
        print(s, end=' ')
        s = addone(s)
    print()