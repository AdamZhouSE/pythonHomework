list1 = input()[1:-1].split(",")
list1 = [int(i) for i in list1]
list1.sort()
i = 0
j = 1
count = 1
max_num = 1
while i < len(list1) - 1:
    j = i + 1
    if list1[j] - list1[i] == 1:
        count += 1
    else:
        count = 1
    if count > max_num:
        max_num = count
    i += 1
print(max_num)