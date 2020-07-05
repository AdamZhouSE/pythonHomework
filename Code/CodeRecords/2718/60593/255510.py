def find(n):
    if(fa[n]==n):
        return n
    else:
        fa[n]=find(fa[n])
        return fa[n]
s=input()
p=eval(input())
fa=list(range(len(s)))
for pp in p:
    ff=find(pp[0])
    fs=find(pp[1])
    if(ff!=fs):
        fa[ff]=fs
res=[[]for i in range(len(s))]
for i in range(len(s)):
    res[find(i)].append(s[i])
for i in range(len(s)):
    res[i].sort()
vis=[False]*len(s)
t=''
for i in range(len(s)):
    t+=res[find(i)][0]
    del res[find(i)][0]
print(t)

