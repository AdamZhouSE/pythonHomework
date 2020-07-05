def tb3():
    n=int(input())
    for i in range(n):
        idno=int(input())
        ids=[int(x) for x in input().split(' ')]
        M=int(input())
        dic={}
        for id in ids:
            if(id in dic):
                dic[id]+=1
            else:dic[id]=1
        a=sorted(dic.items(),key=lambda x:x[1],reverse=False)
        tmp=str(a)[2:-2].split('), (')
        tb_tmp=[]
        for i in range(len(tmp)):
            tb_tmp.append(int(tmp[i].split(', ')[1]))
        cnt=0
        index=-1
        for k in range(len(tb_tmp)):
            cnt+=tb_tmp[k]
            if(cnt>M):
                index=k
                break
        print(len(tb_tmp)-index)


    return

tb3()