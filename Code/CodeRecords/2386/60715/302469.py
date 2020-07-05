def cal(num,p):
    if len(num)<4:
        return 0
    for a in range(len(num)):
        for b in range(len(num)):
            for c in range(len(num)):
                for d in range(len(num)):
                    if a!=b and a!=c and a!=d and b!=c and b!=d and c!=d and num[a]+num[b]+num[c]+num[d]==p:
                        return 1
    return 0
T=int(input())
while T>0:
    n=int(input())
    num = [int(n) for n in input().split()]
    p=int(input())
    print(cal(num,p))
    T-=1