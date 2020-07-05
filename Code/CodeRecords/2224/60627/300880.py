s = list(input())
for i in range(len(s)):
    s[i] = int(s[i])
num = s[:]
num.sort(reverse = True)
if str(num)==str(s):
    print("".join(str(i) for i in s))