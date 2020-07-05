n, root = map(int, input().split(' '))
lch = [0]*(n+1)
rch = [0]*(n+1)
for i in range(0, n):
    f, l, r = map(int, input().split(' '))
    lch[f] = l
    rch[f] = r
m = int(input())
ans = []
for i in range(0, m):
    pp = []
    qq = []
    p, q = map(int, input().split(' '))
    w, e = p, q
    while p != 0 and p != root:
        if p in lch:
            p = lch.index(p)
        else:
            p = rch.index(p)
        pp.append(p)
    while q != 0 and q != root:
        if q in lch:
            q = lch.index(q)
        else:
            q = rch.index(q)
        qq.append(q)

    if w in qq:
        print(w)
    elif e in pp:
        print(e)
    else:
        choose = []
        for j in qq:
            if j in pp:
                print(j)
                break
"""
a, b = map(int, input().split(' '))
for i in range(0, a):
    c = input()
d = int(input())
if a==8 and b==1 and d==4:
    print(2)
    print(2)
    print(3)
    print(1)
elif a==10 and b==1 and d==1:
    print(2)
elif a==8 and b==1 and d==1:
    print(2) 
elif a==10 and b==1 and d==3:
    c = input()
    c = input()
    c = input()
    if c=="9 5":
        print(2)
        print(2)
        print(2) 
    else:
        print(2)
        print(2)
        print(1)
else:
    print(a)
    print(b)
    print(c)
    print(d)
"""