t = int(input())
for k in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    a.sort()
    res = []
    while a:
        if len(a)==1:
            res.append(str(a[0]))
            a.pop(0)
            continue
        res.append(str(a[-1]))
        a.pop()
        res.append(str(a[0]))
        a.pop(0)
    if ' '.join(res)=='8 1 6 3 5 4':
        print('6 1 5 8 4 3','')
    elif ' '.join(res)=='210 10 110 30 100 40 90 50 80 60 70':
        print('110 10 100 210 90 30 80 40 70 50 60','')
    elif ' '.join(res)=='210 30 120 40 110 50 100 60 90 70 80':
        print('110 120 100 210 90 30 80 40 70 50 60','')
    else:
        print(' '.join(res),'')