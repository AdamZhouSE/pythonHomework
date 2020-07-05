s = list(input())
std = list('CODEFESTIVAL2016')
count = 0
for i in range(len(s)):
    if s[i] != std[i]:
        count += 1
print(count)
