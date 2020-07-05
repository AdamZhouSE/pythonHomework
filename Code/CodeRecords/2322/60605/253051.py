# 题目描述
# 如果一个正整数自身是回文数，而且它也是一个回文数的平方，那么我们称这个数为超级回文数。
#
# 现在，给定两个正整数 L 和 R （以字符串形式表示），返回包含在范围 [L, R] 中的超级回文数的数目。
from math import sqrt
def isHuiwen(n: int) -> bool:
    string = list(str(n))
    # print(string)
    rev = string.copy()
    rev.reverse()
    return string == rev

l = int(input())
r = int(input())
cnt = 0
for i in range(l, r+1):
    if not isHuiwen(i):
        continue
    # print(i)
    sq = int(sqrt(i))
    if sq*sq != i:
        continue
    if isHuiwen(sq):
        cnt += 1
print(cnt)