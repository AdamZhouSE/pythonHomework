import re;
#from itertools import *
s = list([int(n) for n in re.findall(r"\-?\d+", input())])
if len(s) == 1:
    print([])
else:
    n = len(s)
    res = []
    while n > 0:
        num = n;
        if s[n-1] == num:
            n -= 1
            continue
        index = -1
        for j in range(n):
            if s[j] == num:
                index = j
                break
        if index != 0:
            res.append(index+1)
            s[:index+1] = s[:index+1][::-1]
        res.append(num)
        s[:num] = s[:num][::-1]
        n -= 1

    print(res)