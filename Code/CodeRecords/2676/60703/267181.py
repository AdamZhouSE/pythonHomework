T = int(input())
for i in range(T):
    NK = [int(x) for x in input().split()]
    N = NK[0]
    K=NK[1]
    numList = [int(x) for x in input().split()]
    maxx = 0
    for m in range(0,N-K+1):
        temp = 0
        for j in range(m,m+K):
            temp+= numList[j]

        if(temp>maxx):
            maxx = temp
    print(maxx)