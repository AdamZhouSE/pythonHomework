'''
字符串S和 T 只包含小写字符。在S中，所有字符只会出现一次。
S 已经根据某种规则进行了排序。我们要根据S中的字符顺序对T进行排序。更具体地说，如果S中x在y之前出现，那么返回的字符串中x也应出现在y之前。
返回任意一种符合条件的字符串T。
'''

import collections

S = str(input())
T = str(input())
count = collections.Counter(T)
res = []

for c in S:
    res.append(c * count[c])
    count[c] = 0

for c in count:
    res.append(c * count[c])

result = "".join(res)
print(result)