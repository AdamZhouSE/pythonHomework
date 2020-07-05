s = list(input())
t = list(input())
f = [0]*256
for i in t:
    f[ord(i)] = 1
ans = "True"
for i in s:
    if f[ord(i)] == 1:
        continue
    else:
        ans = "False"
        break
print(ans)