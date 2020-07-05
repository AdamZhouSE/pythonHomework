list1 = input()[1:-1].split(",")
list1 = [int(i) for i in list1]
list2 = []
for m in range(len(list1) - 1):
    count = 0
    for n in range(m + 1, len(list1)):
        if list1[n] < list1[m]:
            count += 1
    list2.append(count)
list2.append(0)
print(list2)