n = int(input())

orzFang = list(map(int, input().split()))

wormhole = list(map(int, input().split()))

ans=[0]*n

for i in range(n):
    temp=[0]*n

    temp[i]=1
    sum=orzFang[i]
    next1=wormhole[i]-1
    while temp[next1]==0:
        sum+=orzFang[next1]
        temp[next1]=1
        next1=wormhole[next1]-1
    print(sum)
    ans[i]=sum
