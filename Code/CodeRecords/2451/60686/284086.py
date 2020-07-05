list_input = input().split(",")
for i in range(len(list_input)):
    list_input[i] = int(list_input[i])
num = int(input())
index = 0
while list_input[index] < num:
    if index == len(list_input) - 1:
        index = len(list_input)
        break
    else:
        index += 1
print(index)