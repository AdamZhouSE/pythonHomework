nums = int(input())
list_num = []
for i in range(nums):
    num = int(input())
    list_num.append(num)
for i in range(nums):
    num = list_num[i]
    sum = 0
    count = 2
    while sum < num:
        sum += count
        count += 1
    if sum == num:
        count -= 1
    else:
        count -= 2
    output_list = [0] * num
    for j in range(1, count):
        output_list[int(0.5 * j * j + 1.5 * j - 1)] = j
    index = count
    for j in range(len(output_list)):
        if output_list[j] == 0:
            output_list[j] = index
            index += 1
    for j in range(len(output_list) - 1):
        print(output_list[j], end=" ")
    print(output_list[-1])
