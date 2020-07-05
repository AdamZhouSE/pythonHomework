T=int(input())
while T>0:
    m,n,k=map(int,input().split())
    A=[int(n) for n in input().split()]
    B = [int(n) for n in input().split()]
    al=[]
    for i in A:
        al.append(i)
    for i in B:
        al.append(i)
    print(sorted(al)[k-1])
    T-=1