def test():
    t = int(input())
    for _ in range(0, t):
        n = int(input())
        res=func(n)
        print(res)

def func(n):
    if n==1:
        return 1
    else:
        res=func(n-1)
        multi=1
        k=0
        for j in range(1,n):
            k=k+j
        k=k+1
        for i in range(0,n):
            multi=multi*(k+i)
        res=res+multi
        return res

test()