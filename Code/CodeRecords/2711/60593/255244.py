def find(s):
    if(fa[s]==s):
        return s
    else:
        fa[s]=find(fa[s])
        return fa[s]
a=eval(input())
fa={}
for i in a:
    fa[i]=i
for i in range(len(a)):
    for j in range(i):
        cnt=0
        for k in range(len(a[i])):
            if(a[i][k]!=a[j][k]):
                cnt+=1
        if(cnt==2):
            fa[find(a[i])]=fa[find(a[j])]
print(len(list(set(fa.values()))))