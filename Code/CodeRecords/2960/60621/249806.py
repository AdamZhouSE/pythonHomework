te=input().split()
m,n=int(te[0]),int(te[1])
a=input()
b=input()
count=[]
for i in range(n-m+1):
    flag=True
    for j in range(m):
        t1,t2=a[j],b[i+j]
        if(t1=="*" or t2=="*"):
            continue
        elif t1!=t2:
            flag=False
            break
    if(flag):
        count.append(i)
print(len(count))
st=""
for i in count:
    st+=str(i+1)
    st+=" "
print(st)