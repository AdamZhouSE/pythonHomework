def test():
    n=int(input())
    res=[]
    for i in range(0,n):
        line=input().split(',')
        line=list(map(int,line))
        res=res+line
    k=int(input())
    res.sort()
    print(res[k-1])
test()