nums, times = input().split()
nums = int(nums)
times = int(times)
array = []
for i in range(nums):
    array.append(i + 1)
for i in range(times):
    ope = input().split()
    ope = [int(x) for x in ope]
    reverse_list = array[ope[0] - 1:ope[1]]
    reverse_list.reverse()
    for j in range(ope[0] - 1, ope[1]):
        array[j] = reverse_list[j - ope[0] + 1]
for i in range(len(array)):
    if i == len(array) - 1:
        print(array[i], end = ' ')
    else:
        print(array[i], end = ' ')