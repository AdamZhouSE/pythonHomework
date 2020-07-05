num = int(input())
li = []
for i in range(num):
    name = input()
    if name not in li:
        li.append(name)
        print('NO')
    else:
        print('YES')