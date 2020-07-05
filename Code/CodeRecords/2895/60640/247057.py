import re
# 这里会获得['[5,7]']
inp = re.split(r"[\[\],]", input())
# ['', '5', '7', '']
m, n = int(inp[1]), int(inp[2])
res = m
for i in range(m+1, n+1):
    res &= i
print(res)

