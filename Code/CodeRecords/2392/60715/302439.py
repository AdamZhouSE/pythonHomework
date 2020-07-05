def Isthere(num,p):
    for i in num:
        for j in num:
            if p==i*j and i!=j:
                return "Yes"
    return "No"
T=int(input())
while T>0:
    n,p=map(int,input().split())
    num = [int(n) for n in input().split()]
    print(Isthere(num,p))