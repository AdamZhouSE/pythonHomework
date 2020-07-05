T=int(input())
while T>0:
    N=int(input())
    num=[int(n) for n in input().split()]
    num=sorted(num)
    print(num[N-1]*num[N-2]*num[N-3])
    T-=1