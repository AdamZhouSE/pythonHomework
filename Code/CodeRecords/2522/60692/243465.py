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
print(list1)