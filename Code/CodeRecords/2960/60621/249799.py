te=input()
m,n=int(te[0]),int(te[2])
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
if len(count)==0:
    print(a,b)
print(len(count))
st=""
for i in count:
    st+=str(i+1)
    st+=" "
print(st)