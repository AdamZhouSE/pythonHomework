import re
n=int(input())
s1=str(input())
d=s1.count("]")-1
s2=re.findall(r'\d+',s1)
new=[]
a=0
con=[]
for v in s2:
    new.append(int(v))
    a=a+1
    if a==len(s2)/d:
        con.append(new)
        a=0
        new=[]
if len(con) < n - 1:
    print(-1)
    a=-1

parent, res = list(range(n)), n


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])

    return parent[x]


for i, j in con:

    x, y = find(i), find(j)

    if x != y:
        parent[x] = y

        res -= 1
if a!=-1:
    print(res-1)