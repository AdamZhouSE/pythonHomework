from collections import defaultdict
s=input()
pairs=eval(input())
pre=[]
def find(x):
    if(x==pre[x]):return x
    return find(pre[x])

def union(x,y):
    pre[find(y)]=find(x)

for i in range(0,len(s)):
    pre.append(i);

for i in pairs:
    union(i[0],i[1])

mem = defaultdict(list)
for i, v in enumerate(pre):
    mem[find(v)].append(s[i])
for k in mem:
    mem[k].sort(reverse=True)
        
res = []
for i in range(len(s)):
    res.append(mem[find(i)].pop())
print("".join(res))