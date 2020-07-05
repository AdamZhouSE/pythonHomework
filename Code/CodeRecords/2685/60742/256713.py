t = int(input())
for k in range(t):
    n = int(input())
    a = []
    m = n
    while m>0:
        if m>=9:
            a.insert(0,'9')
            m -= 9
        else:
            a.insert(0,str(m))
            m = 0
    for i in range(n):
        a.append('0')
    print(''.join(a))