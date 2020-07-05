import re
lst = re.findall(r'\d',input())
m = int(lst[0])
n = int(lst[1])

res = m
for i in range(m+1,n+1):
    res = res&i
print(res)