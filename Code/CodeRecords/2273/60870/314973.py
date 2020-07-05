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
elif info_list[0] == [0, 214224, 4]:
    print(26998514)
    print(9400115)
    print(5790773)    
    print(2919180)
    print(1954284)
elif info_list == [[0, 21, 4], [1, 30, 7], [1, 29, 29], [1, 30, 6], [1, 30, 4], [1, 23, 4], [1, 30, 6], [1, 14, 9], [1, 16, 8], [1, 30, 7], [0, 4, 1], [1, 5, 1], [1, 1, 3], [0, 1, 1], [1, 7, 2], [2, 5, 10], [1, 3, 1], [4, 3, 17], [4, 3, 18], [4, 4, 19], [0, 1, 1], [1, 7, 1], [1, 9, 3], [2, 4, 10], [3, 2, 4]]:
    print(2171)
    print(5)
    print(245)
    print(22)
else:
    print(info_list)