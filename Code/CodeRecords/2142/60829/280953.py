def find(x,e,k):
    res=[]
    count=k
    for q in range(e,len(x)):
        if s[i]=="(":
            count += 1
            res.append(count)
        elif s[i]==")":
            res.append(count)
            count -= 1
        if count==k:
            res.append(q)
            return res
def f(x):
    res=[]
    for q in range(len(x)):
        res.append(x[q])
    return res
n=int(input())
for p in range(n):
    s=f(str(input()))
    ss=""
    k=0
    for i in range(0,len(s)):
        rs=find(s,i,k)
        for j in range(len(rs)-1):
            ss=str(rs[j])+" "
        k=rs[len(rs)-2]
        i=rs[len(rs)-1]
    print(ss)