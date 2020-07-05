def f(s):
    if s[0]==1:
        s.pop(0)
        return [1]+f(s)
    else:
        a=s.pop(0)
        t=[]
        for i in s:
            if i%s==0:
                t.append(int(i/s))
        if len(f(t))+1>len(f(s)):
            for i in t:
                i*=s
            return  [a]+t
        else:
            return f(s)
        
        
        
print(f([int(x) for x in input().strip().split(',')]))