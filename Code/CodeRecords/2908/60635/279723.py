N=int(input())
src=[]
for i in range(N):
    src.append(input())
p={i:i for i in range(N)}
def f(x):
    if x!=p[x]:
        p[x]=f(p[x])
    return p[x]
for i in range(N-1):
    tmp=set(src[i])
    dic1={}
    for c in tmp:
        dic1[c]=src[i].count(c)
    for j in range(i+1,N):
        if f(i)!=f(j):
            dic2={}
            tmp = set(src[j])
            for c in tmp:
                dic2[c] = src[j].count(c)
            if dic1==dic2:
                p[f(j)]=f(i)
count=0
for index in p:
    if index==p[index]:count+=1
print(count,end='')
