def even_odd(N,a):
    b=[]
    for j in a:
        if j%2==0:
            b.append(j)
            a.remove(j)
    c=b+a
    strc=[str(x) for x in c]
    return ' '.join(strc)
    






T=int(input())
for i in range(T):
    N=int(input())
    info=input().split(' ')
    a=[int(y) for y in info]
    print(a)
    print(even_odd(N,a))
    