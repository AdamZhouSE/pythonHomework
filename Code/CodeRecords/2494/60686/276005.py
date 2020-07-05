str_input = input()
str_input = str_input[1:len(str_input) - 1]
list_int = str_input.split(",")
for i in range(len(list_int)):
    list_int[i] = int(list_int[i])
count = 0
for i in range(len(list_int) - 1):
    for j in range(i + 1, len(list_int)):
        if list_int[i] > pow(2, list_int[j]):
            count += 1
print(count)
