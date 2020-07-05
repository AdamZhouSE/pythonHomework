e=[]
f=[]
g=[]
T=int(input())
for i in range(T):
    a=list(input())
    b=list(input())
    print(a)
    print(b)
    c=[]
    for j in range(len(a)):
        if a[j] not in b:
            c.append(a[j])
    for k in range(len(b)):
        if b[k] not in a:
            c.append(b[k])
    d=list(set(c))
    print(d)
    for m in d:
        if m.isdigit():
            e.append(m)
        else:
            f.append(m)
    e.sort()
    f.sort()
    for h in e:
        g.append(h)
    for l in f:
        g.append(l)
    print(''.join(g))
            
        
    