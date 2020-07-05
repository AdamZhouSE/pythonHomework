list_input = input().split(",")
for i in range(len(list_input)):
    list_input[i] = int(list_input[i])
left_flag = True
right_flag = False
index = 0
res = []
while index < len(list_input):
    if list_input[index] > list_input[index + 1]:
        right_flag = True
    if left_flag and right_flag:
        print(index)
        exit(-1)
    if right_flag and not index >= len(list_input) - 2:
        index += 2
    else:
        index += 1
print(-1)
