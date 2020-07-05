def numop21():
    num=int(input())
    res=''
    while(num!=1 and num!=0):
        res=str(abs(int(num%(-2))))+res
        if(num>0):
            num=int(num/-2)
        else:
            if(num%-2!=0):
                num=int((num/-2)+1)
            else:
                num=int(num/-2)
    if(num==1):
        res='1'+res
    print(res)
    return 0

numop21()