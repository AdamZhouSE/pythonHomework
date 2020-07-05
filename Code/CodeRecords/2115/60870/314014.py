num_group = int(input())
info_list = []
edge_list = []
for i in range(num_group):
    info = input().split()
    info = [int(x) for x in info]
    info_list.append(info)
    for j in range(info[1]):
        edge = input().split()
print(info_list)