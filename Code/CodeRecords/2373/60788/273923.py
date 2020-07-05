def f(s):
    if len(s)<=2:
        return max(s)
    else:
        return max(s[0]+f(s[2:]),f(s[1:]))
a=int(input().strip())
for i in range(a):
    length=int(input().strip())
    li=[int(x) for x in input().strip().split()]
    print(f(li))
        
