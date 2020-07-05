n,q=map(int,input().split(' '))
l=[0 for i in range(q)]
r=[0 for i in range(q)]
c0,cq=0,0
ss=input()
a=[int(i) for i in range(ss.split(' '))]
for i in range(n):
    if a[i]==0:
        c0+=1
    if a[i]==q:
        cq+=1
    if a[i]==0:
        continue
    l[a[i]]=min(l[a[i]],i)
    r[a[i]]=max(r[a[i]],i)
if !c0 and !cq:
    print('NO')
else:
    st=set()
    flag=1
    for i in range(n):
        if i==l[a[i]]:
            st.add(a[i])
        if a[i] and len(st)!=0 and