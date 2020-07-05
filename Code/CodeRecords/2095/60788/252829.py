def f(s,t):
    if len(s)>len(t):
        for i in range(len(s)-len(t)):
            t='0'+t
    if len(t)>len(s):
        for i in range(len(t)-len(s)):
            s='0'+s
    a=list(s)
    b=list(t)
    a.reverse()
    b.reverse()
    Cn=0
    Sn=0
    for i in range(0,len(a
    