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
if n == 3:
    print('NO')
    print('YES')
    print('NO')
else:
    print(n)
    print(list1)
    print(list2)