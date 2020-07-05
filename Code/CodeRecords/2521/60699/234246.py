str=input()
str=str[1:(len(str)-1)]
list=list(map(int,str.split(',')))
dict={}
for i in list:
    if i in dict:
        dict[i]=dict[i]+1
    else:
        dict[i]=1
dict = sorted(dict.items(), key=lambda d: d[1], reverse=True)
dict_temp={}
for i in dict:
    dict_temp[i[0]]=i[1]
dict=dict_temp
res=[]
for i in dict:
    k=dict[i]
    while k>0:
        res.append(i)
        for t in dict:
            if t!=i and dict[t]>0:
                res.append(t)
                dict[t]-=1
                break
        k-=1
print(res)