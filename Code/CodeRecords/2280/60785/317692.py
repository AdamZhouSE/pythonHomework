T=int(input())
while T>0:
    n=int(input())
    num = [int(n) for n in input().split()]
    ls=[]
    while n>0:
        ls.append(n)
        n-=1
    for i in ls:
        if i not in num:
            print(i)
    T-=1