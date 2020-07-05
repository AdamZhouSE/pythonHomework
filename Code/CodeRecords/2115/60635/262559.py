tests = int(input())
p={}


def f(x):
    if x!=p[x]:
        p[x]=f(p[x])
    return p[x]


for t in range(tests):
    info = input().split()
    n = int(info[0])
    m = int(info[1])
    tag=m<n+2
    p={i:i for i in range(2*n)}
    for i in range(m):
        edge = input().split()
        x = int(edge[0])-1
        y = int(edge[1])-1
        p[f(x)]=f(y+n)
        p[f(y)]=f(x+n)
    for i in range(n):
        tag = tag and p[i]!=p[i+n]
        if not tag:
            print('NO')
            break
    else:
        print('YES')