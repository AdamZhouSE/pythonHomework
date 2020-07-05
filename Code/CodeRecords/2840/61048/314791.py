def arr19():
    line1=input().split(" ")
    n,k=int(line1[0]),int(line1[1])
    arr=[int(x) for x in input().split(' ')]
    res=0
    for num in arr:
        s=str(num)
        cnt=0
        for x in s:
            if(x=='4' or x=='7'):
                cnt+=1
        if(cnt<=k):
            res+=1
    print(res)
    return

arr19()