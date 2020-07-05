def kill(n):
    q = []
    for i in range(0, n):
        q.append(i+1)
    p = 0
    for i in range(0, n-1):
        if p == len(q)-1:
            q.pop(0)
            p = 0
        else:
            q.pop(p+1)
            p = (p+1) % len(q)
    return q[0]


count = int(input())
ans = []
for i in range(0, count):
    ans.append(kill(int(input())))
for i in ans:
    print(i)
