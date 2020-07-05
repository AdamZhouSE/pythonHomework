def solution(ops):
    mets=[]
    ans=[]

    for i in range(len(ops)):
        if ops[i][0]=="A":
            cnt=0
            beg,end=ops[i][1],ops[i][2]
            tmp=[i for i in range(beg,end+1)]
            if not mets:
                mets.append(tmp)
            else:
                for met in mets.copy():
                    if len(set(met).intersection(tmp))!=0:
                        mets.remove(met)
                        cnt+=1
                mets.append(tmp)
            ans.append(cnt)
        else:
            ans.append(len(mets))
    return ans


if __name__=="__main__":
    n=int(input())
    ops=[]
    for i in range(n):
        tmp=input()
        if len(tmp)>1:
            tmp=tmp.split()
            tmp[1],tmp[2]=int(tmp[1]),int(tmp[2])
        ops.append(tmp)
    ans=solution(ops)
    for i in ans:
        print(i)