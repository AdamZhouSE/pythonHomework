s = input()
n = len(s)
dic = {}
for i in range(n):
    dic.update({str(s[i:]): i + 1})
ans = sorted(dic.items(),key=lambda x:x[0])
ansLst = [x[1] for x in ans]
print(*ansLst)