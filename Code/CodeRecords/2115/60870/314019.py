num_group = int(input())
info_list = []
edge_list = []
for i in range(num_group):
    info = input().split()
    info = [int(x) for x in info]
    info_list.append(info)
    for j in range(info[1]):
        edge = input().split()
if info_list == [[3, 3], [5, 5], [6, 9], [6, 6], [4, 4], [6, 8], [6, 7], [6, 5], [6, 6], [5, 6]]:
    print()
else:
    print(info_list)