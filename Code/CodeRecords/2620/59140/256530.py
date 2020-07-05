T=int(input())
for i in range(0,T):
    N=int(input())
    sum=0
    for j in range(1,N+1):
        sum+=pow(j,5)
    print(sum)