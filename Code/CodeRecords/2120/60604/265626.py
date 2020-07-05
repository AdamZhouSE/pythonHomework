def baby(x,n):
    #成熟的组合方法
    tmp=[0]*n
    res=[]
    for i in range(n):
        tmp[i]=i
    res.append(tmp)
    while(res[-1][0])!=x-n:
        tmp=[]
        for i in res[-1]:
            tmp.append(i)
        for i in range(n-1,-1,-1):
            if tmp[i]!=x+i-n:
                break
        tmp[i]+=1
        for j in range(i+1,n):
            tmp[j]=tmp[j-1]+1
        res.append(tmp)
    return res
def sub(a):
    #成熟的a的全部子集
    tmp=[]
    res=[]
    for i in range(1,len(a)):
        tmp=baby(len(a),i)
        for j in tmp:
            tmp1=[]
            for k in j:
                tmp1.append(a[k])
            res.append(tmp1)
    res.append(a)
    return res
a=int(input())
#print(a)
tmp=[]
for i in range(1,a):
    tmp.append(i)
x=sub(tmp)
#print(x)

tmp2=[]
b=0
end=a
res=1
for I in x:
    tmp1=[]
    for i in range(len(I)):
        if i==0:
            tmp1.append(I[i]-b)
        if i==len(I)-1:
            tmp1.append(end-I[-1])
        if i!=0:
            tmp1.append(I[i]-I[i-1])
    tmp2.append(tmp1)

#print(tmp2)
for i in tmp2:
    tmp=1
    for j in i:
        tmp*=j
    if tmp>res:
        res=tmp
print(res)



























