nums, times = input().split()
nums = int(nums)
times = int(times)
array = []
for i in range(nums):
    array.append(i + 1)
for i in range(times):
    ope = input().split()
    ope = [int(x) for x in ope]
    index1 = array.index(ope[0])
    index2 = array.index(ope[1])
    if index1 < index2:
        reverse_list = array[index1:index2 + 1]
        reverse_list.reverse()
        for j in range(index1, index2 + 1):
            array[j] = reverse_list[j - index1]
    else:
        reverse_list = array[index2:index1 + 1]
        reverse_list.reverse()
        for j in range(index2, index1 + 1):
            array[j] = reverse_list[j - index2]
for i in range(len(array)):
    if i == len(array) - 1:
        print(array[i])
    else:
        print(array[i], end = ' ')