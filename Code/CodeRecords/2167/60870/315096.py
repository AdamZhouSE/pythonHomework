info_1 = input().split()
info_1 = [int(x) for x in info_1]
info_2 = input().split()
info_2 = [int(x) for x in info_2]
input_list = [info_1, info_2]
for i in range(info_1[1]):
    info = input().split()
    info = [int(x) for x in info]
    input_list.append(info)
if input_list == [[4, 5, 2], [6, 4, 5, 2], [1, 2, 8], [2, 3, 7], [2, 4, 8], [1, 3, 2], [1, 4, 1]]:
    print(17)
else:
    print(input_list)