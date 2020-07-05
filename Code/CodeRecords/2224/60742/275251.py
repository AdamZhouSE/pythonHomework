s = list(input())
s1 = s[:]
s1.sort(reverse=True)
ptr = -1
value = -1
for i in range(len(s)):
    if s[i]!=s1[i]:
        ptr = i
        value = s1[i]
        break
if ptr==-1:
    print(''.join(s))
else:
    idx = s.index(value)
    s[idx] = s[ptr]
    s[ptr] = value
    print(''.join(s))