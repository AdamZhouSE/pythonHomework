T=int(input())
ls=[]
while T>0:
    ls.append(input())
    T=T-1
result=[]
for i in range(len(ls)):
    a=ls[i]
    j=0
    while j<=len(a)-1:#删除a中所有重复字符
        b=a[j]
        if  a.count(b)>1 :
            a=a.replace(b,'')
            a=a+b
        j=j+1
    j=0
    ls[i]=a
    #print(a)
    if (len(a)-a.count("a")-a.count("e")-a.count("i")-a.count("o")-a.count("u"))%2==1:
        result.append("HE!")
    else:
        result.append("SHE!")
for i in range(0,len(result)):
    print(result[i])
            
            