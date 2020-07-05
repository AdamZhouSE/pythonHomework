def judge(list1, list2):
    list1.sort()
    list2.sort()
    for j in range(len(list2)):
        if list2[j] != list1[j]:
            return False
    return True


str_input = input()
str_input = str_input[1:len(str_input) - 1]
list_input = str_input.split(",")
list_order = []
for i in range(len(list_input)):
    list_input[i] = int(list_input[i])
    list_order.append(list_input[i])
list_order.sort()
start = 0
count = 1
for i in range(len(list_input) - 1):
    if judge(list_input[start:i + 1], list_order[start:i + 1]):
        start = i + 1
        count += 1
    else:
        continue
print(count)
