num_test = int(input())
info_list = []
array_list = []
for i in range(num_test):
    info = input()
    array = input().split()
    array = [int(x) for x in array]
    info_list.append(info)
    array_list.append(array)
for i in range(num_test):
    array = array_list[i]
    maxMul = array[0] * array[1] * array[2]
    for j in range(len(array) - 2):
        for k in range(j + 1, len(array) - 1):
            for p in range(k + 1, len(array)):
                if array[j] * array[k] * array[p] >= maxMul:
                    maxMul = array[j] * array[k] * array[p]
    print(maxMul)