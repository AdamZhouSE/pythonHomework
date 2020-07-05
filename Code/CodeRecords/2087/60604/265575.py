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
def gcd(a,b):
    for i in range(1,a+1):
        if a%i==0 and b%i==0:
            res=i
    return res
n=input()
a=[]
for I in range(int(n)):
    a.append(int(input()))
tmp=sub(a)
res=[1]
for i in tmp:
    j=True
    for j in range(len(i)-1):
        for k in range(j+1,len(i)):
            if gcd(i[j],i[k])*gcd((i[j]+1),(i[k]+1))==1:
                j=False
                break
    if j:
        res.append(len(i))
print(res[-1],end="")
'''if (res[-1]!=1):
    
    print(sub([1,3,5,6]))
    print(a)
    print(tmp)
'''








































