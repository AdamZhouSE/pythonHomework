for i in range(0,eval(input())):
    l = eval(input())
    lis = list(map(int,input().split(' ')))
    lis = sorted(lis)
    res = 0
    temp = 1
    for i in range(0,l-1):
        if lis[i]+1==lis[i+1]:
            temp+=1
        else:
            if temp>res:
                res=temp
            temp=1
    print(res)