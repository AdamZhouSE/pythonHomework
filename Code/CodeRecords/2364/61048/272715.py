def numop29():
    num=int(input())
    res=0
    for x in range(1,num+1):
        if followednum(x)==True:
            res+=1
    print(res)

    return


def followednum(num):
    string=str(num)
    res=False
    for i in range(len(string)):
        for j in range(i+1,len(string)):
            if(string[i]==string[j]):
                res=True
                break

    return res

numop29()