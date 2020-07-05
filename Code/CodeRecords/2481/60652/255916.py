T=int(input())
for i in range(0,T):
    N,M=map(int,input().split())
    l1=list(map(int,input().split()))
    l2=list(map(int,input().split()))
    a=[]
    for m in l1:
        if m in l2 and m not in a:
            a.append(m)
    print(len(a))        