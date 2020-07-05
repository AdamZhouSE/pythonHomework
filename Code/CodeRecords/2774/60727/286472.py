for i in range(0,eval(input())):
    nk = input().split(' ')
    li = input().split(' ')
    n=int(nk[0])
    k=int(nk[1])
    li=list(map(int,li))
    res = 0
    temp=0
    sorted(li)
    for i in li:
        if temp+i<=k:
            res+=1
            temp+=i
    print(res)