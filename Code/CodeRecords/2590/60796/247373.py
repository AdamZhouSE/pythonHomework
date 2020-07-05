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
        if a.count(b)>1:
            a=a.replace(b,'')
            a=a+b
        j=j+1
    ls[i]=a
    print(a)
    if len(a)%2==0:
        result.append("SHE!")
    else:
        result.append("HE!")
for i in range(0,len(result)):
    print(result[i])
            
            