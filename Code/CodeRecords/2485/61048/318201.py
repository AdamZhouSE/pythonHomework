def tb9():
    n=int(input())
    for i in range(n):
        k=int(input())
        set=[]
        tmp=input().split(' ')
        for i in tmp:
            str_tmp="".join(sorted([x for x in i]))
            set.append(str_tmp)
        dic={}

        for word in set:
            if word in dic:
                dic[word]+=1
            else:dic[word]=1
        a = sorted(dic.items(), key=lambda x: x[1], reverse=False)
        tmp = str(a)[2:-2].split('), (')
        tb_tmp = []
        for i in range(len(tmp)):
            tb_tmp.append(int(tmp[i].split(', ')[1]))
        res=""
        for num in tb_tmp:
            res+=str(num)+" "
        print(res[:-1])
    return

tb9()