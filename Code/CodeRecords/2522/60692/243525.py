list1 = input()[1:-1].split(",")
list2 = input()[1:-1].split(",")
list1 = [int(i) for i in list1]
list2 = [int(j) for j in list2]
m = 0
for i in list2:
    n = m + 1
    while n < len(list1):
        if list1[m] == i:
            m += 1
        elif list1[m] != i and list1[n] == i:
            list1[m], list1[n] = list1[n], list1[m]
        n += 1
for p in range(m, len(list1) - 1):
    for q in range(p + 1, len(list1)):
        if list1[p] > list1[q]:
            list1[p], list1[q] = list1[q], list1[p]
print(list1)