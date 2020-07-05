a=eval(input())
for i in range(a):
    b=input()
    b=[int(x) for x in input().split()]
    c=[int(x) for x in input().split()]
    d=set(b)
    d.update(set(c))
    le=len(set(b))+len(set(c))-len(d)
    print(le)