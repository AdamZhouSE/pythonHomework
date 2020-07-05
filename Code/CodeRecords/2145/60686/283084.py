nums = int(input())
list_all = []
for i in range(nums):
    length = int(input())
    input_list = input().split(" ")
    for j in range(length):
        input_list[j] = int(input_list[j])
    list_all.append(input_list)
for i in range(nums):
    input_list = list_all[i]
    maximum = 0
    cap = 0
    for j in range(1, len(input_list)):
        for k in range(len(input_list) - j + 1):
            cap = j * min(input_list[k:k + j])
            if cap > maximum:
                maximum = cap
    print(maximum)
