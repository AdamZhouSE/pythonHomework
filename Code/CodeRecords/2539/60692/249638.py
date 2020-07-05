list1 = input()[1:-1].split(",")
list1 = [int(i) for i in list1]
list2 = list1[:]
list2.sort()
p = 0
q = len(list1) - 1
while p < q:
    if list1[p] == list2[p]:
        p += 1
    if list1[q] == list2[q]:
        q -= 1
    if list1[p] != list2[p] and list1[q] != list2[q]:
        break
print(q - p + 1)