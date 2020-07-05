def f(s):

    if len(s) == 1:
        return s
    elif len(s)==2:
        if s[1]%s[0]==0:
            return s
        else:
            return s[0:1]
    else:
        a = s.pop(0)
        t = []
        for i in s:
            if i % a == 0:
                t.append(int(i / a))
        h=t.copy()
        k=s.copy()
        if len(f(t)) + 1 >= len(f(s)):
            for i in range(len(h)):
                h[i] *= a
            return [a] + f(h)
        else:
            return f(k)


print(f([int(x) for x in input().strip().split(',')]))