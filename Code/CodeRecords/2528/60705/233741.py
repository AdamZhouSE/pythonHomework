# 按升序排列
input_array = list(map(int, input().split("[")[1].split("]")[0].split(",")))
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
