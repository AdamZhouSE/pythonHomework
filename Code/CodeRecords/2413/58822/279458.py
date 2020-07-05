import math
def bin(a,n):
    if(a==0):
        return str(0)*n
    k=1
    sum=a%2
    while((a/2)!=0):
        a=int(a/2)
        k=k*10
        sum=k*(a%2)+sum
    res=""
    res=str(sum)
    while(len(res)!=n):
        res="0"+res
    return res
def yuan(a):
    sum=0
    u=1
    for i in range(0,len(a)):
        sum=sum+u*sum[len(a)-1-i]
    return sum
def com(a,b):
    tong=0
    yi=0
    for i in range(len(a)):
        if(a[i]==b[i]):
            tong+=1
        else:
            yi+=1
    return yi

a=int(input())#010#位数
b=int(input())#101#开始
li=[]
st=[]
le=int(math.pow(2,a))
k=int(math.pow(2,a))
for i in range(0,le):
    li.append(int(i))
    st.append(bin(i,a))
le=int(math.pow(2,a))
res=[]
res.append(b)
m=bin(b,a)
cu=bin(b,a)
res1=[]
flag=1
g=0
while((len(res))!=le):
    for i in range(len(li)-1,-1,-1):
        if(com(cu,st[i])==1 and st[i]!=m):
            if(flag!=1):
                flag-=1
                g+=1
                continue
            cu=st[i]
            res.append(li[i])
            del li[i]
            del st[i]
            break
    if(len(res)==le):
        if com(m,cu)==1:
            break
        else:
            flag=flag+g+1
            g=0
            res1=res.copy()
            res=[]
            res.append(b)
            cu=m
print(res)