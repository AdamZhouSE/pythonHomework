inp = input()
ans = ''
dic = {inp[0]: 0}
for i in inp:
    dic[i] = 0
for i in inp:
    dic[i] += 1
for i in [t[0] for t in sorted(dic.items(), key=lambda x: x[1], reverse=True)]:
    for j in range(dic[i]):
        ans += i
print(ans)
