n=int(input())
for x in range(0,n):
    num=int(input())
    numbers=list(map(int,input().split(" ")))
    res=[0]*num
    result=-1
    for i in range(0,num):
        if not res.__contains__(numbers[i]):
            res[i]=numbers[i]
        else:
            result=res.index(numbers[i])+1
    print(result)