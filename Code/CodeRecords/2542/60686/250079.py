input_array = input()
input_array = input_array[1:len(input_array) - 1]
list_input = input_array.split(",")
for i in range(len(list_input)):
    list_input[i] = int(list_input[i])
list_input.sort()
count = 1
maximum = 0
for i in range(1, len(list_input)):
    if list_input[i] == list_input[i - 1] + 1:
        count += 1
        if count>maximum:
            maximum = count
    else:
        count = 0
print(maximum)