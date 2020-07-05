N=int(input())
value=[int(n) for n in input().split(' ')]
road=[int(n) for n in input().split(' ')]
result=[]

for i in range(1,N+1):
    pre=[]
    x=road[i-1]
    pre.append(x)
    sum=value[i-1]
    if x==i:
        result.append(sum)
    else:
        while x!=i:
            sum=sum+value[x-1]
            x=road[x-1]
            if x in pre:
                break
            else:
                pre.append(x)
        result.append(sum)
for i in range(0,N):
    print(result[i])

