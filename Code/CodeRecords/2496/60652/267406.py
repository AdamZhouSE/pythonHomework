def re():
    s=input()
    s=sorted(sorted(s), key=lambda x: s.count(x), reverse=True)
    n = len(s) // 2
    if len(s)%2==0:
        if s.count(s[0])>n:
            return ''
        a, b = s[:n], s[n:]
        for i in range(len(b)):
            s[i * 2] = b[i]
        for i in range(len(a)):
            s[i * 2 + 1] = a[i]
    else:
        if s.count(s[0])>n+1:
            return ''
        a,b=s[:n],s[n+1:]
        mid=s[n]
        for i in range(len(a)):
            s[i * 2] = a[i]
        for i in range(len(b)):
            s[i * 2 + 1] = b[i]
        s[len(s)-1]=mid
    return ''.join(s)


print(re())