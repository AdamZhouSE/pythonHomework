'''
给定一个字符串，请将字符串里的字符按照出现的频率降序排列。
'''

from collections import Counter

s = str(input())
res = ''.join(i * j for i, j in Counter(s).most_common())
print(res)