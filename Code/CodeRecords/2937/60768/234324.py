l = list(input())
s = list("CODEFESTIVAL2016")
num = 0
for i in range(16):
    if l[i] != s[i]:
        num = num + 1

print(num)