str0 = "CODEFESTIVAL2016"
str1 = input().strip()
res = 0
for i in range(16):
    if str0[i]!=str1[i]:
        res += 1
print(res)