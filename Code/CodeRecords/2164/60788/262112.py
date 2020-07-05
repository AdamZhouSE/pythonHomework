def f(s):
    m=set(list(s))
    n=0
    for i in m:
        n+=s.count(i)-1
    return n


a=int(input().strip())
for i in range(a):
    print(f(input().strip()))
    