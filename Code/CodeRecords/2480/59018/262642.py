def even_odd(N,a):
    b=[]
    for j in a:
        if j%2==0:
            b.append(j)
            a.pop(j)
    c=b+a
    return c
    






T=int(input())
for i in range(T):
    N=int(input())
    info=input().split(' ')
    a=[int(y) for y in info]
    print(even_odd(N,a))
    