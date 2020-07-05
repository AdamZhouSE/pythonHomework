def f(s):
    if len(s)<=2:
        return 0
    else:
        while s[0]<=s[1]:
            s.pop(0)
            if len(s)<=2:
                return 0
            
        while s[len(s)-1]<=s[len(s)-2]:
            s.pop()
            if len(s)<=2:
                return 0
        if max(s)>max(s[0],s[len(s)-1]):
            return f(s[0:s.index(max(s))+1])+f(s[s.index(max(s))+1:])
        else:
            t=min(s[0],s[len(s)-1])*len(s)
            for k in s:
                if k>=min(s[0],s[len(s)-1]):
                    t-=min(s[0],s[len(s)-1])
                else:
                    t-=k
            return t
a=int(input().strip())
for i in range(a):
    length=int(input().strip())
    t=[int(x) for x in input().strip().split()]
    print(f(t))