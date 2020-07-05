s = input()
t = [i for i in input()]
ans = ''
for i in range(len(s)):
    cnt = t.count(s[i])
    for j in range(cnt):
        t.remove(s[i])
        ans += s[i]
for i in t:
    ans += i
print(ans)
