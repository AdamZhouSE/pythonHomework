def arr13():
    n=int(input())
    dis=[int(x) for x in input().split(" ")]
    line3=input().split(' ')
    s,t=int(line3[0]),int(line3[1])
    if(s>t):
        s,t=t,s
    res=0
    for x in range(s-1,t-1):
        res+=dis[x]
    sumD=sum(dis)
    res=res if(sumD-res>res)else sumD-res
    print(res)
    return

arr13()