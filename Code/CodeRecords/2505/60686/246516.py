list_input = input().split(",")
for i in range(len(list_input)):
    if list_input.count(list_input[i]) == 2:
        print(list_input[i])
        break