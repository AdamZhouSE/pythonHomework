from collections import Counter

s = str(input())
res = ''.join(i * j for i, j in Counter(s).most_common())
print(res)