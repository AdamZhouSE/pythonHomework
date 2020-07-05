def numop19():
    x=float(input())
    n=int(input())
    res=0
    if(n>0):
        res=1
        for i in range(n):
            res=res*x
    else:
        res=1
        for i in range(0-n):
            res=res*(1/x)
    print('{:.5f}'.format(res))
    return 0

numop19()