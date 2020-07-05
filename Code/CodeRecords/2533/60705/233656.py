input_array = list(map(int, input().split("[")[1].split("]")[0].split(",")))
for i in range(0, len(input_array)):
    if (int)(input_array[i]) % 2 == 1:
        input_array.append(input_array[i])
        input_array.pop(i)
print(input_array)