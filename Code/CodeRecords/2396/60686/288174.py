nums = int(input())
list_input = input().split(" ")
for i in range(nums):
    list_input[i] = int(list_input[i])
res = []
for i in range(nums):
    index = list_input.index(min(list_input[i:len(list_input)]))
    list_temp = list_input[i:index + 1]
    list_temp = list_temp[::-1]
    for j in range(0, i):
        list_input[j] = list_input[j]
    for j in range(i, len(list_temp) + i):
        list_input[j] = list_temp[j - i]
    res.append(index + 1)
for i in range(len(res)):
    print(res[i], end=" ")

