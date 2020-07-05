import collections
s=input()
pairs=eval(input())
p=list(range(len(s)))
def find(i):
    if i!=p[i]:
        p[i]=find(p[i])
    return p[i]
def union(i,j):
    p[find(i)]=find(j)
for i,j in pairs:
    union(i,j)        
dic=collections.defaultdict(list)
for i in range(len(p)):           
    dic[find(i)].append(i)
res=list(s)
for lst in dic.values():
    for i, c in zip(lst, sorted(res[i] for i in lst)):
        res[i] = c
print(''.join(res))