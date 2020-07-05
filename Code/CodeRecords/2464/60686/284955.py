num = int(input())
list_input = input().split(",")
for i in range(len(list_input)):
    list_input[i] = int(list_input[i])
for i in range(len(list_input)):
    for j in range(len(list_input) - i + 1):
        if sum(list_input[j:j + i]) == num:
            print(i)
            exit(0)

 