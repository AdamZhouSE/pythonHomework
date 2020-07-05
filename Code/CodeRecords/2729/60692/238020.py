list1 = input()[1:-1].split(",")
i = 0
j = len(list1) - 1
while i < j:
    if list1[i] == list1[i + 1]:
        i += 2
    if list1[j] == list1[j - 1]:
        j -= 2
print(list1[i])