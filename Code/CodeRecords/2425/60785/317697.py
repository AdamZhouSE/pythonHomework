T=int(input())
while T>0:
    N,K=input().split()
    N=int(N)
    K=int(K)
    num = [int(n) for n in input().split()]
    re=abs(num[0]-K)
    ls=[num[0]]
    for i in num:
        if abs(i-K)<re:
            del ls[:]
            ls.append(i)
            re=abs(i-K)
        elif abs(i-K)==re:
            ls.append(i)
    print(max(ls))
    T-=1