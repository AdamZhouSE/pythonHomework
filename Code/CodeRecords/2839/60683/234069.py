n = eval(input())
names = {}
for i in range(n):
    name = input()
    if names.get(name) is None:
        print('NO')
        names.update({name: 0})
    else:
        print('YES')