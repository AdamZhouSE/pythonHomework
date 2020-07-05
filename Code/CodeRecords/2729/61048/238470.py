def search1():
    a=input()

    str=list(a[1:len(a)-1].split(','))

    dic={}
    for i in range(0,len(str)):
        if(str[i]) in dic.keys():
            dic[str[i]]=dic[str[i]]+1
        else:
            dic[str[i]]=1

    for word in dic.keys():
        if(dic.get(word)==1):
            res=word
    return res
b=[1,1,22,3,3,4,4]
print(search1())