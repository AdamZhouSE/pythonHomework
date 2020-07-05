list1 = input()[1:-1].split(",")
for i in range(len(list1)):
    list1[i] = int(list1[i])
count = 0
for j in range(len(list1)):
    for k in range(j + 1, len(list1)):
        if list1[j] > list1[k] * 2:
            count += 1
print(count)