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
le=(2**a)
for i in range(0,le):
    li.append(int(i))

l=[]
index=0
res=[]
for i in li:
    s=str(i)
    temp=[]
    if len(l)==0:
        temp.append(s)
    else:
        for j in l:
            for k in range(len(j) + 1):
                temp.append(j[:k]+s+j[k:])
    l=temp
for i in range(len(l)):
    arr=list(l[i])
    if(int(arr[0])!=b):
        continue
    st=[]
    for k in range(len(arr)):
        st.append(bin(int(arr[k]),a))
    flag=1
    for j in range(0,len(arr)-1):
        if((com(st[j],st[j+1]))!=1):
            flag=0
            break
    if(flag==1 and int(arr[0])==b and com(st[0],st[(len(arr)-1)])==1):
        res=list(map(int,arr))
        break
print(res)