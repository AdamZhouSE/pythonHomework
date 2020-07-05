def numop20():
    num=int(input())
    res=1
    if(num%2==0 or num%5==0):
        res=-1
    else:
        for i in range(1,num+1):
            if(res%num==0):
                res=i
                break
            else:
                res=res*10+1
    print(res)
    return 0

numop20()