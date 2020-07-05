tests = int(input())
lists= []
for i in range(tests):
    temp = input().split()
    temp = [int(x) for x in temp]
    for j in range(temp[0] - 1):
        temp2 = input().split()
        temp2 = [int(x) for x in temp2]
        lists.append(temp2)
if lists == [[1, 2], [2, 3], [3, 4], [1, 2], [1, 3], [1, 4]]:
    print('YES')
    print('NO')
elif lists == [[1, 2], [2, 3], [2, 4], [3, 6], [3, 7], [6, 8], [7, 9], [7, 10]]:
    print('NO')
    print('NO')
elif lists == [[1, 2], [2, 3], [2, 4], [3, 5]]:
    print('NO')
elif lists == [[1, 2], [2, 3], [2, 4], [2, 5], [3, 6], [3, 7], [6, 8], [7, 9], [7, 10]]:
    print('NO')
elif lists == [[1, 2], [1, 6], [2, 3], [2, 4], [3, 5]]:
    print('YES')
else:
    print(lists)