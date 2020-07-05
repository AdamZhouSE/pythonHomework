info_1 = input().split()
info_1 = [int(x) for x in info_1]
info_2 = input().split()
info_2 = [int(x) for x in info_2]
input_list = [info_1, info_2]
for i in range(info_1[1]):
    info = input().split()
    info = [int(x) for x in info]
    input_list.append(info)
print(input_list)