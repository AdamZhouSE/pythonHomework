s = input()
t = input()
rul = []
for i in range(0,len(s)):
    for j in range(0,len(t)):
        if s[i]==t[j]:
            rul.append(t[j])
for j in range(0,len(t)):
    if t[j] in rul:
        continue
    else:
        rul.append(t[j])
print(''.join(rul))
