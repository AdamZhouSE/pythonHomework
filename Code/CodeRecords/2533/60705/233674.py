input_array = list(map(int, input().split("[")[1].split("]")[0].split(",")))
length = len(input_array)
count = 0
for i in range(0, length):
    if input_array[i] % 2 == 0:
        count += 1
i = 0
while i < count:
    if (int)(input_array[i]) % 2 == 1:
        input_array.append(input_array[i])
        input_array.pop(i)
        i = i - 1
    i = i + 1
print(input_array)
