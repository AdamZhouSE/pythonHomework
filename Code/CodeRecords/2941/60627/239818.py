# 8
input()
s = input()
t = 0
for i in range(len(s)):
    if s[i] == 'A':
        t += 4
    if s[i] == 'B':
        t += 3
    if s[i] == 'C':
        t += 2
    if s[i] == 'D':
        t += 1
    if s[i] == 'F':
        t += 0
print('%f.14'.format{t/len(s)})