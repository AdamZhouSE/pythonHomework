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
a=input().split(",")
for i in range(len(a)):
    a[i]=int(a[i])
#print(a)
tmp=sub(a)
res=[]
for i in tmp:
    if len(i)==1:
        res.append(i)
    else:
        j=True
        for j in range(0,len(i)-1):
            if i[j]>=i[j+1]:
                j=False
                break
        if j:
            res.append(i)
#print(res)

print(len(res[-1]))
'''if len(res[-1])==6 :
    print(a)
    print(res[-1])
    '''
           

























    