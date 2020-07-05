list1 = list(input())
list2 = [i + 1 for i in range(len(list1))]
for j in range(len(list1) - 1, 0, -1):
    for k in range(j - 1, -1, -1):
        if list1[j] > list1[k] or (list1[j] == list1[k] and list2[j] < list2[k]):
            list1[j], list1[k] = list1[k], list1[j]
            list2[j], list2[k] = list2[k], list2[j]
list2.reverse()
list2 = [str(i) for i in list2]
print(" ".join(list2))