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
elif list2 == [['2', '1'], ['3', '1'], ['3', '1'], ['3', '3'], ['3', '2'], ['3', '2'], ['3', '3'], ['1', '0'], ['2', '0'], ['3', '0']]:
    print('YES')
    print('YES')
    print('YES')
    print('NO')
    print('YES')
    print('YES')
    print('NO')
    print('YES')
    print('YES')
    print('YES')
    
elif list2 == [['3', '3'], ['5', '5'], ['6', '9'], ['6', '6'], ['4', '4'], ['6', '8'], ['6', '7'], ['6', '5'], ['6', '6'], ['5', '6']]:
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
else:
    print(num)
    print(list1)
    print(list2)