def test():
    t=int(input())
    for _ in range(0,t):
        w=int(input())
        res=fibonacci(w)
        print(res)

def fibonacci(n):
    if n==1 :
        return 1
    elif n==2:
        return 2
    tmp=0
    pre=1
    res=2
    for i in range(2,n):
        tmp=res
        res=res+pre
        pre=tmp
    return res
        

test()
