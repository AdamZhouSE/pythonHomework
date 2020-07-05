import math


def isHuiWen(s):
    for i in range(len(s)):
        j = len(s) - 1 - i
        if j < i:
            break
        if s[i] != s[j]:
            return False
    return True
L = int(input())
R = int(input())
re = 0
for i in range(L, R + 1):
    s1 = str(i)
    s2 = str(math.sqrt(i))
    s3 = s2[s2.index(".")+1:]
    if s3=="0":
        if isHuiWen(s1) and isHuiWen(s2[:s2.index(".")]):
            re=re+1
print(re)
