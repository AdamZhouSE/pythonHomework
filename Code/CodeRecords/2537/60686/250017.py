input_array = input()
input_array = input_array[1:len(input_array) - 1]
list_input = input_array.split(",")
n = int(input())
for i in range(len(list_input)):
    list_input[i] = int(list_input[i])
list_input.sort()
print(list_input[len(list_input) - n])
