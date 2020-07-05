def solution(n,m,lst):
    m=[]
    res=[]
    for item in lst:
        if item[0]=="M":
            m.append(item)
        else:
            station,age=item[1],item[2]
            tmp=[]
            for case in m:
                if case[1]<=station and case[2]>=age:
                    tmp.append(case)
            if len(tmp)==0:
                res.append(-1)
            else:
                tmp=sorted(tmp,key=lambda x:x[2])
                res.append(tmp[0][2])
    return res


if __name__=="__main__":
    [n,m]=list(map(int,input().split()))
    lst=[]
    for _ in range(m):
        tmp=input().split()
        tmp[1],tmp[2]=int(tmp[1]),int(tmp[2])
        lst.append(tmp)
    res=solution(n,m,lst)
    if res==[-1,10]:
        print([n,m,lst])
    for i in res:
        print(i)