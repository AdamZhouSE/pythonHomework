def numop6():
    num=input()
    res=''
    for i in range(0,len(num)):
        if(num[i]=='6'):
            res=num[0:i]+'9'+num[i+1:]
            break
    print(res)
    return

numop6()