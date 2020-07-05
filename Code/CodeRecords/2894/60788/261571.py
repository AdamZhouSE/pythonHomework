def f(s):
    if len(s)==1:
        return 0
    if s.find('V')<0:
        return 1
    else:
        t=0
        for i in range(len(s)-1):
            if list(s)[i]=='V' and list(s)[i+1]=='K':
                t+=1
        return t
    
def g(s):
    t=[f(s)]
    for i in range(len(s)):
        if s[i]=='K':
            t.append(f(s[0:i]+'V'+s[i+1:]))
        else:
            t.append(f(s[0:i]+'K'+s[i+1:]))
    return max(t)

a=int(input().strip())
s=input().strip()
print(g(s),end='')