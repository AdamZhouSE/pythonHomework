s = list(input())
for i in range(len(s)):
    s[i] = int(s[i])
num = s[:]
num.sort()
print(s)
if num==s:
    print(s)