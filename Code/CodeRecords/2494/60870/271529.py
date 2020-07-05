str_input = input()
str_input = str_input[1:-1]
array = str_input.split(',')
array = [int(x) for x in array]
count = 0
for j in range(0, len(array) - 1):
    for k in range(j + 1, len(array)):
        if array[j] > 2 * array[k]:
            count = count + 1
print(count)