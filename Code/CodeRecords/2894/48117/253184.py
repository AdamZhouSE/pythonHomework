length = int(input())
s = input()
count = 0

for i in range(length - 1):
    if s[i] == 'V' and s[i + 1] == 'K':
        count += 1
        s.replace(s[i], 'x')
        s.replace(s[i + 1], 'x')

for j in range(length - 1):
    if s[j] != 'x' and s[j] == s[j + 1]:
        count += 1
        break

print(count, end='')