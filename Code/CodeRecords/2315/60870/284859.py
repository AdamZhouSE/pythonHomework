node_dict = {}
nums = int(input())
for i in range(nums - 1):
    info_list = input().split()
    parent = info_list[0]
    child = info_list[1]
    if i == 0:
        node_dict[parent] = 1
        node_dict[child] = 2
    else:
        node_dict[child] = node_dict[parent] + 1
height = max(node_dict.values())
print(height)