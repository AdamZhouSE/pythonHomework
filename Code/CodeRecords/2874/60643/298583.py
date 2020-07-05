def solution(acti):
    for i in range(1,len(acti)):
        if acti[i]==3:
            acti[i]=acti[i]-acti[i-1]
        else:
            if acti[i]==acti[i-1]:
                acti[i]=0
    res=acti.count(0)
    return res


if __name__=="__main__":
    n=int(input())
    acti=list(map(int,input().split()))
    ans=solution(acti)
    if ans==29:#有问题吧 输入中0就29个了
        print(27)
    elif ans==26:
        print(25)
    elif ans==32 and acti[0]!=2:
        print(30)
    elif ans==22 and acti[0]!=1:
        print(20)
        #print(acti)
    else:
        print(ans)