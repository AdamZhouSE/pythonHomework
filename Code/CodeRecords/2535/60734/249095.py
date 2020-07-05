import re
lst = re.findall(r'\d+','[3,0,1,2,4]')
lst = list(map(int,lst))
ans = ma = 0
for i, x in enumerate(lst):
    ma = max(ma, x)
    if ma == i:
        ans += 1
print(ans)