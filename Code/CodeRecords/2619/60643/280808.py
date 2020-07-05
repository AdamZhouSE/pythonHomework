def isLuckyNum(s):
    s=list(s)
    subStrs=list(s[0])
    s=s[1:]
    for i in range(len(s)):
        length=len(subStrs)#这个很重要 不然下面循环会死循环
        for j in range(length):
            subStrs.append(subStrs[j]+s[i])
        subStrs.append(s[i])
    subStrs=["".join(x) for x in subStrs]#集合,列表不是可哈希元素,但字符串是,所以subsets中的元素必须先转为str再对subsets进行集合运算

    #计算乘积
    mul=[]

    for i in subStrs:
        length=len(i)
        if length==1:
            mul.append(int(i))
        else:
            temp=1
            for j in i:
                temp*=int(j)
            mul.append(temp)
    if len(mul)!=len(set(mul)):
        return 0
    return 1


if __name__=="__main__":
    n=int(input())
    cnt=0
    res=0
    while cnt<n:
        s=input()
        res=isLuckyNum(s)
        cnt+=1
        print(res)