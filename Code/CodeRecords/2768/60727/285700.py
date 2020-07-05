for i in range(0,eval(input())):
    a=input().split(' ')
    a=list(map(int,a))
    res=0
    for i in range(a[0],a[1]+1):
        if i%a[2]==0:
            res+=1
    print(res)