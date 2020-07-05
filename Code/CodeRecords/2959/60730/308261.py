s1 = input()
s2 = input()
cnt = 0
if len(s1) > len(s2):
    s1, s2 = s2, s1
for i in range((len(s1))):
    for k in range(1,len(s1)):
        if i + k > len(s1):
            break
        for j in range(len(s2)):

            if s1[i:i + k] == s2[j:j + k] :
                cnt += 1
if len(s1) == 1 and len(s2) > 1:
    for i in range(1, len(s2)):
        if s1 == s2[i]:
            cnt += 1
print(cnt)
