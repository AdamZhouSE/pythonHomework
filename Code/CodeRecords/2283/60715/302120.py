T=int(input())
while T>0:
    n=int(input())
    num = [int(n) for n in input().split()]
    num=sorted(num)
    t=0
    for i in num:
        t+=1
        if t!=len(num):
            print(i,end=' ')
        else:
            print(i)
    T-=1