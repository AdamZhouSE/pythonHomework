#10
import itertools
from itertools import permutations,combinations

ori = input().split(",")
pList = list(permutations(ori))
# print(pList)
strs = []
for item in pList:
    s = ""
    for i in item:
        s += i
    # if s <= "2359": 这样只能排除>24的小时，分钟无法保证正确
    if s[0:2] <= "23" and s[2:4] <= "59":
        strs.append(s)
strs.sort(reverse=True)
if len(strs) != 0 :
    tar = strs[0]
    print(tar[0:2]+":"+tar[2:4])
else:
    print("")
