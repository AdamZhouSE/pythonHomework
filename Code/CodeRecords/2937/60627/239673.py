# 3
s = input()
ini = "CODEFESTIVAL2016"
t = 0
for i in range(len(s)):
    if s[i] != ini[i]:
        t += 1
print(t)