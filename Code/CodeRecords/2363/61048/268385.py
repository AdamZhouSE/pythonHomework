def numop7():
    num=int(input())
    numb = bin(num)[2:]
    for i in range(0,len(numb)):
        if(numb[i]=='0'):
            numb=numb[0:i]+'1'+numb[i+1:]
        else:
            numb=numb[0:i]+'0'+numb[i+1:]
    res=int('0b'+numb,2)
    print(res)
    return


numop7()