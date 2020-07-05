list_input = input().split(",")
for i in range(len(list_input)):
    list_input[i] = int(list_input[i])
list_input.sort()
print(list_input[0])
