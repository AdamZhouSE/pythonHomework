n = int(input())
names = []
for i in range(n):
    name = input()
    if name in names:
        print('YES')
    else:
        print('NO')
        names.append(name)
