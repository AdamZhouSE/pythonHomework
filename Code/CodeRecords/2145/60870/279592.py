num_test = int(input())
info_list = []
array_list = []
for i in range(num_test):
    info = int(input())
    array = input().split()
    array = [int(x) for x in array]
    info_list.append(info)
    array_list.append(array)
for i in range(num_test):
    array = array_list[i]
    area_list = []
    for j in range(len(array)):
        k = j
        wide = 1
        while k - 1 >= 0:
            k = k - 1
            if array[k] >= array[k + 1]:
                wide = wide + 1
            else:
                break
        k = j
        while k + 1 < len(array):
            k = k + 1
            if array[k] >= array[k - 1]:
                wide = wide + 1
            else:
                break
        area_list.append(array[j] * wide)
    maxArea = max(area_list)
    print(maxArea)