n=int(input())
temp={''}
for i in range(n):
    name=input()
    if (name in temp):
        print('YES')
    else:
        print('NO')
    temp.add(name)