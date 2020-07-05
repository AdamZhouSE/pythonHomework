#23
from itertools import permutations
num = input()
p = list(permutations(num,len(num)))
allNums = []
allPosi = []
for item in p:
    s = ""
    if item[0] == '0':
        continue
    for ob in item:
        s += ob
    allNums.append(int(s))
for item in allNums:
    n = str(pow(item, 1 / 2))
    flag = True
    ind = n.index(".")
    s = n[ind + 1:]
    for i in range(0, len(s)):  # 检验小数点后有没有非0数
        if s[i] != "0":
            flag = False
            break
    allPosi.append(flag)
if True in allPosi:
    print(True)
else:
    print(False)