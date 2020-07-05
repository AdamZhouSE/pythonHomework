
coordinates = []

co_len = int(input())
for i in range(co_len):
    coordinates.append([int(j) for j in input().split(",")])
k_dot_dict = {}
k_not_exit_index = set()
for i in range(0, co_len - 1):
    for j in range(i + 1, co_len):
        if coordinates[i][0] == coordinates[j][0]:
            k_not_exit_index.add(i)
            k_not_exit_index.add(j)
        else:
            k = (coordinates[j][1] - coordinates[i][1]) / (coordinates[j][0] - coordinates[i][0])
            if not k_dot_dict.__contains__(k):
                k_dot_dict[k] = set()
                k_dot_dict[k].add(j)
                k_dot_dict[k].add(i)
            else:
                k_dot_dict[k].add(i)
                k_dot_dict[k].add(j)
num_list = [len(k_not_exit_index)]
for i in k_dot_dict.items():
    num_list.append(int(len(i[1])))
print(max(num_list))