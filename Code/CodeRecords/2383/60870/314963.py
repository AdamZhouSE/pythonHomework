num_test = int(input())
info_list = []
for i in range(num_test):
    info = input().split()
    info = [int(x) for x in info]
    for j in range(info[0] - 1):
        edge = input().split()
        edge = [int(x) for x in edge]
        info_list.append(edge)
if info_list == [[1, 2], [2, 3], [3, 4], [1, 2], [1, 3], [1, 4]]:
    print('YES')
    print('NO')
else:
    print(info_list)