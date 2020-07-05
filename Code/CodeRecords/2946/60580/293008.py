a = input()
i = 0
result = 0
while i < len(a):
    if i == len(a) - 1:
        break
    if a[i + 1] != a[i]:
        result += 1
    i += 1
if a[-1] == '0':
    result += 1
print(result)
