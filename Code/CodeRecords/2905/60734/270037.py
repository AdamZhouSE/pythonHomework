import re
lst = re.findall(r'\d+',input())
res = 0
base = 0
for x in lst[::-1]:
    res += int(x)*(2**base)
    base+=1
print(res)