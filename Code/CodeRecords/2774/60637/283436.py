tests=(int)(input())
for i in range(tests):
    n,k=map(int,input().split(' '))
    cost=list(map(int,input().split(' ')))
    list.sort(cost)
    sum=0
    i=0
    while(i<n and sum<=k):
        sum+=cost[i]
        i+=1
    print(i-1)