t = int(input())
result = []
for i in range(t):
    a = list(set(list(input())))
    b = list(set(list(input())))
    tmp = ''
    for j in a:
        if j not in b:
            tmp += j
    for j in b:
        if j not in a:
            tmp += j
    result.append(''.join(sorted(list(tmp))))
print(*result)
print()
