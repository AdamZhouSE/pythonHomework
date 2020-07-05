def solution(data):
    st=set(data)
    tms=[]
    dic={}
    for i in st:
        tmp=data.count(i)
        #if tmp not in dic:
        dic.setdefault(tmp,[]).append(i)

    lst=list(dic.items())
    lst=sorted(lst,key=lambda x:x[0],reverse=True)
    res=[]
    for item in lst:
        nums=sorted(item[1])
        for i in nums:
            for _ in range(item[0]):
                res.append(i)
    return res


if __name__=="__main__":
    n=int(input())
    for _ in range(n):
        length=int(input())
        data=list(map(int,input().split()))
        ans=solution(data)
        ans=[str(x) for x in ans]
        print(" ".join(ans),end="")
        print(" ")