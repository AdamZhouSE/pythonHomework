child = int(input())
favor = input().split(' ')
favor = [int(x) - 1 for x in favor]

exist = False
for i in range(child):
    if favor[favor[i]] != i and favor[favor[favor[i]]] == i:
        print('YES')
        exist = True
        break

if not exist:
    print('NO')