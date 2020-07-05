list_input = input().split(",")
for i in range(len(list_input)):
    list_input[i] = int(list_input[i])
num = int(input())
res = []
for i in range(0, len(list_input) - 1):
    for j in range(i + 1, len(list_input)):
        if list_input[i] + list_input[j] == num:
            res.append(i + 1)
            res.append(j + 1)
            print(res)
            exit(0)
if len(res) == 0:
    print("None")