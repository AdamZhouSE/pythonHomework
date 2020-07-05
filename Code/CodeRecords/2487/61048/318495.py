
def tb11():
    n=int(input())
    for k in range(n):
        k=int(input())
        candis=input().split(' ')
        dic={}
        for candi in candis:
            if(candi not in dic):
                dic[candi]=1
            else:dic[candi]+=1
        a = sorted(dic.items(), key=lambda x: x[1], reverse=True)
        tmp = str(a)[2:-2].split('), (')
        tb_tmp = []
        for i in range(len(tmp)):
            tb_tmp.append([tmp[i].split(', ')[0][1:-1],tmp[i].split(', ')[1]])
        set=[]

        for i in tb_tmp:
            if i[1]==tb_tmp[0][1]:
                set.append([i[0],i[1]])
        set.sort(key=lambda x:x[0])

        res=""
        res+=set[0][0]+" "+set[0][1]
        print(res)
    return

tb11()