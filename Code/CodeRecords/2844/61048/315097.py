def arr21():
    line1=input().split(' ')
    n,t=int(line1[0]),int(line1[1])
    time=[int(x) for x in input().split(" ")]
    res=0
    temp,cnt=0,0
    for i in range(n):
        for j in range(i,n):
            if(temp+time[j]<=t):
                if(j==n-1):
                    cnt+=1
                    if(res<cnt):
                        res=cnt
                    cnt,temp=0,0
                cnt+=1
                temp+=time[j]
            else:
                if(res<cnt):
                    res=cnt
                cnt,temp=0,0
                break
    print(res)
    return

arr21()