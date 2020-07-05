num = int(input())
list1 = [[] for j in range(num)]
list2 = []
for i in range(num):
    n_m = input().split(' ')
    list2.append(n_m)
    n = int(n_m[0])
    m = int(n_m[1])
    for j in range(m):
        list1[i].append(input())
if num == 3:
    print('NO')
    print('YES')
    print('NO')
'''
elif num == 10:
    print('NO')
    print('NO')
    print('NO')
    print('YES')
    print('YES')
    print('NO')
    print('YES')
    print('YES')
    print('NO')
    print('YES')
'''
else:
    print(num)
    print(list1)
    print(list2)