str_input = input()
str_input = str_input[1:len(str_input) - 1]
list_input = str_input.split(",")
for i in range(len(list_input)):
    list_input[i] = int(list_input[i])
maximum = 1
length = 1
for i in range(len(list_input) - 1):
    if list_input[i] < list_input[i + 1]:
        length += 1
        if length > maximum:
            maximum = length
    else:
        length = 1
print(maximum)
