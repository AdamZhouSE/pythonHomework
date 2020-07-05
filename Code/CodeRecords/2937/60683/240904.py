standard = 'CODEFESTIVAL2016'
s = input().strip()
res = 0
for i in range(16):
    if s[i] != standard[i]:
        res += 1
print(res)
