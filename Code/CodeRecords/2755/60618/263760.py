t=int(input())
for i in range(t):
    a1,a2=map(int,input().split())
    m=[int(j) for j in input().split()]
    n=[int(j) for j in input().split()]
    re=[0]*(a1+a2-1)
    for j in range(0,a1):
        for k in range(0,a2):
            re[j+k]+=a[j]*a[k]
    print(re)       
    