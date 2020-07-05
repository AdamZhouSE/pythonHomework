n = int(input())
s = input()
vv = False
ans = 0
for i in range(n - 1):
    if s[i:i + 2] == 'VK':
        ans += 1
    elif s[i:i + 2] == 'VV':
        vv = True
if vv: ans += 1
print(ans, end='')