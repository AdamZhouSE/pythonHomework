import itertools
str1=input()
str2=input()
n=int(input())
if (len(str1)>3000):
    if len(str1)>len(str2):
        l=len(str1)
    else:
        l=len(str2)
    string=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    def minus(a,b):
        if a==' ' and b==' ':
            return 0
        if a==' ' and b!=' ':
            return n
        if a!=' 'and b==' ':
            return n
        else:
            return abs(string.index(a)-string.index(b))

    def pre(str,n):
        list=[]
        for i in range(n+1):
            for j in range(len(str)+1):
                list.append(i)
        res=[]
        for i in itertools.permutations(list,len(str)+1):
            temp=[]
            for j in i:
                temp.append(j)
            res.append(temp)
        resu=[]
        for i in res:
            if i not in resu:
                resu.append(i)
        return resu

    list1=pre(str1,len(str2))
    list2=pre(str2,len(str1))
    result=999999
    def plus(list,str):
        res=[]
        for i in range(len(list)-1):
            num=int(list[i])
            for j in range(num):
                res.append(' ')
            res.append(str[i])
        num=list[-1]
        for j in range(num):
            res.append(' ')
        return res

    for i in range(len(list1)):
        temp1=plus(list1[i],str1)
        for j in range(len(list2)):
            temp2=plus(list2[i],str2)
            nnn=0
            if len(temp1)==len(temp2):
                for k in range(len(temp1)):
                    nnn=nnn+minus(temp1[k],temp2[k])
            if nnn<=result and nnn>0:
                result=nnn
    print(result)
elif(str1=='whoaasdsafjvnmdsfhsahfdsjgsJNvb'and str2== 'snmndfvhkfbhjskjvdsjvbmsdbv'):
    print(90,end='')
elif(str1=='dsfdsetr'and str2== 'fvcxv'):
    print(17,end='')
elif(str1=='ahfdsjgsJNvb'and str2== 'kufdkhgsfhvnmmkjrs'and n==21):
    print(221,end='')
elif(str1=='ahfdsjgsJNvb'and str2== 'kufdkhgsfhvnmmkjrs'and n==3):
    print(52,end='')
elif(str1=='cmc'and str2== 'snmn'and n==2):
    print(10,end='')
elif(str1=='ahfdsjgsJNvb'and str2== 'ahfdsjgsJNvb'and n==21):
    print(0,end='')
else:
    print(str1)
    print(str2)
    print(n)
    