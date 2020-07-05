def f(s):
    if s[0]==1:
        s.pop(0)
        return [1]+f(s)
    elif len(s)==1:
        return s
    else:
        a=s.pop(0)
        t=[]
        for i in s:
            if i%a==0:
                t.append(int(i/a))
        if len(f(t))+1>len(f(s)):
            for i in t:
                i*=a
            return  [a]+t
        else:
            return f(s)
        
        
        
print(f([int(x) for x in input().strip().split(',')]))