def series(n):
    m=1
    if n==1:
        return m*2
    for i in range(1,n):
        m=m*2
    return m
q=int(input())
for i in range(q):
    n=int(input())
    answer=series(n)
    print(answer)