info = input().split()
info = [int(x) for x in info]
info_list = []
for i in range(info[1]):
    info_input = input().split()
    info_list.append(info_input)
print(info_list)