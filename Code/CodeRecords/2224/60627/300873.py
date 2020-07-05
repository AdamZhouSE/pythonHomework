s = list(input())
for i in range(len(s)):
    s[i] = int(s[i])
num = s[:]
num.sort()
if str(num)==str(s):
    print(s)