import math

s = input()
length = len(s)

if length == 1:
    if s == '0':
        print(0)
    else:
        print(1)
    exit()

ans = 0

latter = int(s[1:])
if s[0] == '1':
    ans += latter + 1
elif s[0] == '0':
    pass
else:
    ans += int(math.pow(10, length - 1))

for i in range(1, length - 1):
    pre = int(s[:i])
    latter = int(s[i + 1:])
    if s[i] == '1':
        ans += pre*int(math.pow(10, length - i - 1)) + latter + 1
    elif s[i] == '0':
        ans += pre*int(math.pow(10, length - i - 1))
    else:
        ans += pre*int(math.pow(10, length - i - 1)) + int(math.pow(10, length - i - 1))

pre = int(s[:length - 1])
if s[length - 1] == '0':
    ans += pre
else:
    ans += pre + 1

print(ans)