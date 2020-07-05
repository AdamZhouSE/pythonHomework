s = list(input().strip())
dic = {}
sz = len(s)
for i in range(sz):
    if dic.get(s[i]) is None:
        dic.update({s[i]: 1})
    else:
        dic[s[i]] += 1
res = sorted(dic.items(), key=lambda x: x[1], reverse=True)
# print(res)
seq = []
for i in res:
    if i[1] + i[1] - 1 > sz:
        break
    seq.extend(i[0] * i[1])
ans = []
i = 0
j = len(seq) - 1
while i <= j:
    ans.append(seq[i])
    i += 1
    if i <= j:
        ans.append(seq[j])
        j -= 1
print(''.join(ans))
