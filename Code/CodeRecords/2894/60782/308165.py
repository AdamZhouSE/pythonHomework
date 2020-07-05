
n = int(input())
ans = 0
s = input()
for i in range(n - 1):
    if s[i] == 'V' and s[i + 1] == 'K':
        ans += 1
        
        s_li = list(s)
        s_li[i] = 'v'
        s_li[i + 1] = 'k'
        s = str(s_li)
        
for j in range(n - 1):
    if s[j] == s[j + 1]:
        ans += 1
print(ans)
