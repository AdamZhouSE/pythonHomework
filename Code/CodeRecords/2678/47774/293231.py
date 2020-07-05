t=int(input())
for i in range(t):
    n=int(input())
    bn=bin(n)
    num=bn.count('1',0)
    if num==1:
        print(bn.index('1'))
    else:
        print(-1)