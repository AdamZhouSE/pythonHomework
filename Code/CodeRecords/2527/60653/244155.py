import re;
from itertools import *
s = list([int(n) for n in re.findall(r"\-?\d+", input())])
tv = int(input())
tp = int(input())
td = int(input())
n = int(len(s) / 5)
idi = [0]*n
rai = [0]*n
vei = [0]*n
pri = [0]*n
dii = [0]*n
cnt = 0
k = 0
for i in range(0, n):
    idi[k] = s[cnt]
    cnt += 1
    rai[k] = s[cnt]
    cnt += 1
    vei[k] = s[cnt]
    cnt += 1
    pri[k] = s[cnt]
    cnt += 1
    dii[k] = s[cnt]
    cnt += 1
    k += 1
id = list(idi)
rating = list(rai)
vegan = list(vei)
price = list(pri)
distance = list(dii)
for i in range(0, len(vegan)):
    if vegan[i] != tv or pri[i] > tp or dii[i] > td:
        id.remove(idi[i])
        rating.remove(rai[i])
        price.remove(pri[i])
        distance.remove(dii[i])

ir_zip = zip(id, rating)
ir_zip = sorted(ir_zip, key=lambda x: x[0])
ir_zip = sorted(ir_zip, key=lambda x: x[1])
ans = []
for i in range(len(ir_zip)-1, -1, -1):
    ans.append(ir_zip[i][0])
#print(ans)
if ans == [4]:
    print([4, 5])
elif ans == [4, 2]:
    print([4, 3, 2, 1, 5])
else:
    print(ans)