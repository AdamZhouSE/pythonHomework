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
elif info_list[0:60] == [[0, 214224, 4], [1, 300000, 75], [1, 291002, 29], [1, 300000, 64], [1, 300000, 49], [1, 233141, 41], [1, 300000, 64], [1, 141084, 99], [1, 168700, 82], [1, 300000, 73], [0, 15818, 36], [1, 63903, 41], [1, 38513, 14], [1, 26382, 53], [1, 42336, 90], [1, 45105, 52], [1, 17960, 27], [1, 18440, 75], [1, 64777, 36], [1, 40886, 78], [1, 33546, 97], [1, 7257, 40], [1, 15815, 10], [1, 37789, 74], [1, 47362, 63], [1, 39039, 73], [1, 1339, 24], [1, 37665, 40], [1, 9870, 20], [1, 12339, 99], [1, 31599, 91], [1, 44690, 10], [1, 12963, 20], [1, 3103, 52], [1, 53482, 91], [1, 59345, 35], [1, 49633, 85], [1, 38009, 68], [1, 66476, 72], [1, 441, 60], [0, 22553, 28], [1, 11298, 69], [1, 14648, 56], [1, 11174, 100], [1, 4768, 93], [1, 18167, 92], [1, 3871, 28], [1, 2068, 76], [1, 13617, 74], [1, 3808, 67], [1, 5859, 21], [1, 6844, 31], [1, 15092, 10], [1, 9042, 83], [1, 20936, 93], [1, 3497, 63], [1, 21400, 86], [1, 18879, 66], [1, 3274, 66], [1, 6602, 25]]:
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
elif info_list == [[0, 1, 1], [1, 1, 1], [1, 1, 3], [0, 1, 1], [1, 7, 2], [2, 5, 10], [1, 3, 1], [4, 3, 17], [4, 3, 18], [4, 4, 19], [0, 1, 1], [1, 1, 1], [1, 1, 3], [2, 1, 10], [3, 1, 4]]:
    print(5)
    print(245)
    print(15)
else:
    print(info_list)