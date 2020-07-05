import collections
s=input()
pairs=eval(input())
p= list(range(len(s)))
def find(x):
    if x!=p[x]:
        p[x]= find(p[x])
    return p[x]
for i, j in pairs:
    px, py = find(i), find(j)
    if px != py:
        p[px] = py
mem = collections.defaultdict(list)
for i, v in enumerate(p):
    mem[find(v)].append(s[i])
for k in mem:
    mem[k].sort(reverse=True)
result= []
for i in range(len(s)):
    result.append(mem[find(i)].pop())
print("".join(result))
    