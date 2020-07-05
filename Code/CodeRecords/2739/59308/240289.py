import re
title = input()
pattern = re.compile('[0-9]+')
a = pattern.findall(title)
a = [int(x) for x in a]
k = a[0]
n = a[1]
res = list()
tmp_ = list()
s = 0


def dfs(start, temp, s):
    for i in range(start, n):
        s += i
        temp.append(i)
        if s == n:
            if len(temp) == k:
                res.append(temp.copy())
            else:
                temp.pop(len(temp)-1)
                return
        elif s > n:
            s -= i
            temp.pop(len(temp)-1)
            return
        else:
            dfs(i+1, temp, s)
        s -= i
        temp.pop(len(temp)-1)


dfs(1, tmp_, 0)
print(res)

