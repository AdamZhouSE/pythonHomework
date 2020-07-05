list1 = input().split(",")
list1.insert(1, list1[0][1:])
list1.remove(list1[0])
list1.insert(-1, list1[-1][0:-1])
list1.remove(list1[-1])
list2 = []
for i in range(len(list1)):
    list1[i] = int(list1[i])
for j in range(0, len(list1) - 1):
    count = 0
    k = j + 1
    while k <= len(list1) - 1:
        if list1[k] < list1[j]:
            count += 1
        k += 1
    list2.append(count)
list2.append(0)
print(list2)