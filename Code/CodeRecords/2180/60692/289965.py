s1 = input()
s2 = input()
cnt = 0
if s1 == s2:
    cnt += 1
for i in range(1, len(s1)):
    for j in range(0, len(s1) - i + 1):
        cnt += s2.count(s1[j: j + i])
print(cnt)