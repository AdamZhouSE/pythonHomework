import collections
s=input()
src=input()
src=src[2:len(src)-2].split('],[')
pairs=[[int(i[0]),int(i[2])]for i in src]

p={i:i for i in range(len(s))}

def f(x):
    if x!=p[x]:
        p[x]=f(p[x])
    return p[x]

for i,j in pairs:
    p[f(j)]=f(i)
dict=collections.defaultdict(list)
for i,j in enumerate(map(f,p)):
    dict[j].append(i)
ans=list(s)
for q in dict.values():
    tmp=sorted(ans[i] for i in q)
    for i,j in zip(sorted(q),tmp):
        ans[i]=j
print (''.join(ans))
    
