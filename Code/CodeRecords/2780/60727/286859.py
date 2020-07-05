for i in range(0,eval(input())):
    num = eval(input())
    li=list(map(int,input().split(' ')))
    k=eval(input())
    res=1
    for i in li:
        res*=i
    print(res%k)