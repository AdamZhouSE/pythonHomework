n = int(input())
names = []
for i in range(n):
    names.append(input())
for i in range(n):
    if names[i] in names[:i]:
        print('YES')
    else:
        print('NO')