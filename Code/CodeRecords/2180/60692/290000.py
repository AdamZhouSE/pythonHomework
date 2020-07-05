s1 = input()
s2 = input()
cnt = 0
if s1 == s2:
    cnt += 1
t1 = set(s1)
for x in t1:
    cnt += s1.count(x) * s2.count(x)
for i in range(2, len(s1)):
    j = 1
    temp = s1[0:i]
    while j < len(s1) - i + 1:
        if s1[j:j+i] != temp:
            cnt += s1.count(temp) * s2.count(temp)
            temp = s1[j:j + i]
        j += 1
    cnt += s1.count(temp) * s2.count(temp)
print(cnt,end="")