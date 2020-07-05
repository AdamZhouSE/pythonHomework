n = list(input())
line = [[''] * len(n)] * len(n)
for i in range(0, len(n)):
    for j in range(i, len(n)):
        line[i] = n[i:] + n[0:i]

for i in range(1, len(n)):
    for j in range(0, len(n) - i):
        if ''.join(line[j]) > ''.join(line[j + 1]):
            line[j], line[j + 1] = line[j + 1], line[j]

re = ''
for m in range(0, len(n)):
    re += line[m][len(n) - 1]
print(re,end='')