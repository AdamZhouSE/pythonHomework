def j1(x,a):
    for i in range(len(x)):
        if x[i]>a:
            return False
    return True
def j2(x,a):
    for i in range(len(x)):
        if x[i]<a:
            return False
    return True
n=int(input())
for p in range(n):
    a=int(input())
    b=[int(x) for x in input().split(" ")]
    c=j2(b,b[0])
    d=j1(b,b[a-1])
    if c and d:
        print(0)
    elif not c and not d:
        print(2)
    else:
        print(1)