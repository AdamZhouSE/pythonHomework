t=eval(input())
for _ in range(t):
    arr=list(map(int,input().strip().split(' ')))
    x=arr[0]
    y=arr[1]
    z=arr[2]
    scoreA=0
    scoreB=0
    while z!=1:
        if x%z==0:
            x-=1
            scoreA+=1
        elif y%z==0:
            y-=1
            scoreB+=1
        else:
            z-=1
    print(scoreA,end=' ')
    print(scoreB)
            