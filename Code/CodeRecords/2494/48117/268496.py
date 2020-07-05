rawStr = input()
s = rawStr[1:-1].split(',')

for i in range(len(s)):
    s[i] = int(s[i])

count = 0
for i in range(len(s) - 1):
    for j in range(i + 1, len(s)):
        if s[i] > s[j] * 2:
            count += 1

print(count)