list1 = input()[1:-1].split(",")
list1 = [int(i) for i in list1]
i = 0
j = 1
while j < len(list1):
    if list1[i] % 2 != 0 and list1[j] % 2 == 0:
        list1[i], list1[j] = list1[j], list1[i]
        i += 1
    elif list1[i] % 2 == 0:
        i += 1
    j += 1
print(list1)