temp = input().split()
a = int(temp[0])
b = int(temp[1])
ar = 10 * [0]
for i in range(a, b + 1):
    if i == 0:
        continue
    s = str(i)
    for c in s:
        ar[int(c)] += 1

ans = ''

for x in ar:
    ans += str(x) + ' '
print(ans.strip(' '), end='')
