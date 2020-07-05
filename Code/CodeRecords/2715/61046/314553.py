
import collections
temp=list(input())
size=-1
t=[]

com=[]
for x in temp:
    if x==']':
        size+=1
lst=[[0]*2 for i in range(size)]
for x in temp:
    if(x!='[' and x!=']' and x!=',' and x!=' '):
        t.append(x)
for i in range(size):
    for j in range(2):
        lst[i][j]=int(t[i*2+j])

m = 0
row = collections.defaultdict(set)
col = collections.defaultdict(set)

for i, j in lst:
    row[i] |= {j}
    col[j] |= {i}
    m = max(m, i)

graph = 0
for i in range(m + 1):
    if i in row:
        graph += 1
        stack = {i}
        while stack:
            x = stack.pop()
            for j in row[x]:
                if j in col:
                    stack |= col[j]
                    del col[j]
            del row[x]

print(len(lst) - graph)