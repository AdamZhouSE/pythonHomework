def f(s):
    if len(s) == 1:
        return [s]
    else:
        start=s[0]
        t=f(s[1:])
        for x in t:
            if x[0]>start:
                x.insert(0,start)
        return t




s = [int(x) for x in input().split(',')]
if max(len(x) for x in f(s))==3:
    print(s)
print(max(len(x) for x in f(s)))