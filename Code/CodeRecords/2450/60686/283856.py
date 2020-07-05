list_input = input().split(",")
for i in range(len(list_input)):
    list_input[i] = int(list_input[i])
num = int(input())
if list_input.count(num) == 0:
    print("[-1, -1]")
elif list_input.count(num) == 1:
    print("[", end="")
    print(list_input.index(num), end=", ")
    print(list_input.index(num), end="")
    print(']')
else:
    print("[", end="")
    print(list_input.index(num), end=", ")
    print(list_input.index(num, list_input.index(num) + 1), end="")
    print(']')
