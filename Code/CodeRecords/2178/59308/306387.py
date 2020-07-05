import re
n = int(input())
pattern = re.compile('[0-9]+')
a = [int(x) for x in pattern.findall(input())]
res = list()
temp = list()
for i in range(len(a)):
    temp.append(a[i])
    for j in range(len(temp)):
        if temp[j:] not in res:
            res.append(temp[j:])
    print(len(res))



