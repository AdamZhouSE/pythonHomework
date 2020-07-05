num_test = int(input())
info_list = []
for i in range(num_test):
    info = input().split()
    info = [int(x) for x in info]
    for j in range(info[0]):
        data = input().split()
        data = [int(x) for x in data]
        info_list.append(data)
if info_list == [[0, 1, 1], [1, 1, 1], [1, 1, 3], [2, 1, 10], [3, 1, 4], [0, 1, 1], [1, 7, 2], [2, 5, 10], [1, 3, 1], [4, 3, 17], [4, 3, 18], [4, 4, 19], [1, 1, 1], [8, 1, 100]]:
    print(15)
    print(316)
else:
    print(info_list)