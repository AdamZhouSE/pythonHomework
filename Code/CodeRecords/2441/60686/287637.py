str_input = input()
str_input = str_input[1:len(str_input) - 1]
list_input = str_input.split(",")
for i in range(len(list_input)):
    list_input[i] = int(list_input[i])
list_input.sort()
print("[", end="")
for i in range(len(list_input) - 1):
    print(list_input[i], end=", ")
print(list_input[-1], end="")
print("]")
