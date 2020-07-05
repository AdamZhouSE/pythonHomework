a=input()
a=a[2:len(a)-2]
b=a.split('],[')
tickets=[]
for i in range(len(b)):
    c=b[i].split(',')
    tickets.append(c)
from collections import defaultdict
dest = defaultdict(list)
for k, v in sorted(tickets)[::-1]:
    dest[k] += v,
res = list()
stack = ['JFK']
while stack:
    while dest[stack[-1]]:
        stack.append(dest[stack[-1]].pop())
    res.append(stack.pop())
print(res[::-1])