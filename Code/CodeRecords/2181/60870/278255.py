num_test = int(input())
index_list = []
for i in range(num_test):
    index = int(input())
    index_list.append(index)
for i in range(num_test):
    index = index_list[i]
    res = index * index * index + index
    print(res)