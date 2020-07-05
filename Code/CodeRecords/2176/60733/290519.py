s = input()
dic = dict()
n = len(s)
for i in range(n):
    dic[s[i:]] = i + 1
r = sorted(dic)
res = ""
for item in r:
    res = res +str(dic[item])+" "
res = res[:-1]
print(res)