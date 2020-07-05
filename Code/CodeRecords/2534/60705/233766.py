# 合并k个排序数组，返回合并后的数组
input_array = list(map(int, input().replace("[", "").replace("]", "")))
length = len(input_array)
i = 1
while i < length:
    if input_array[i] < input_array[i-1]:
        temp = input_array[i]
        input_array[i] = input_array[i-1]
        input_array[i-1] = temp
        i = 0
    i = i + 1
print(input_array)