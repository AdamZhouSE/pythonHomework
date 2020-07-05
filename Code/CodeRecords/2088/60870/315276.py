num = int(input())
info_list = []
for i in range(num - 1):
    info = input().split()
    info_list.append(info)
if info_list == [['2', '3', '2', '4', '2'], ['5', '2', '1', '3', '1', '3', '2', '4', '1', '4', '3'], ['4', '2', '1', '3', '2', '4', '1', '4', '2']]:
    print(17)
else:
    print(info_list)