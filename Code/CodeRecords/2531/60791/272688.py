from collections import Counter
s = input()
dic = dict(Counter(s))
a = sorted(dic.items(), key=lambda x: x[1], reverse=True)
res = ''
for item in a:
    res += item[0]*item[1]
print(res)