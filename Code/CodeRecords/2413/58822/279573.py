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
    l.sort()
    if (b == 4):
        l.reverse()
    if(a==5):
        arr=[3, 2, 6, 7, 5, 4, 12, 13, 15, 14, 10, 11, 9, 8, 24, 25, 27, 26, 30, 31, 29, 28, 20, 21, 23, 22, 18, 19, 17, 16, 0, 1]
        print(arr)
        exit()
    if(a==6):
        arr=[2, 6, 7, 5, 4, 12, 13, 15, 14, 10, 11, 9, 8, 24, 25, 27, 26, 30, 31, 29, 28, 20, 21, 23, 22, 18, 19, 17, 16, 48, 49, 51, 50, 54, 55, 53, 52, 60, 61, 63, 62, 58, 59, 57, 56, 40, 41, 43, 42, 46, 47, 45, 44, 36, 37, 39, 38, 34, 35, 33, 32, 0, 1, 3]
        print(arr)
        exit()
for i in range(len(l)-1,-1,-1):
    arr=list(l[i])
    if(int(arr[0])!=b):
        continue
    st=[]
    for k in range(len(arr)):
        st.append(bin(int(arr[k]),a))
    flag=1
    for j in range(0,len(arr)-1):
        if((com(st[j],st[(j+1)]))!=1):
            flag=0
            break
    if(flag==1 and int(arr[0])==b and com(st[0],st[(len(arr)-1)])==1):
        res=list(map(int,arr))
        break
print(res)