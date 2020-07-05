list1 = input().split(",")
list1.insert(1, list1[0][1:])
list1.remove(list1[0])
list1.insert(-1, list1[-1][0:-1])
list1.remove(list1[-1])
for i in range(len(list1)):
    list1[i] = int(list1[i])
list1.sort()
max = 0
if len(list1) <= 1:
    max = 0
else:
    j = 0
    while j < len(list1) - 1:
        if list1[j + 1] - list1[j] > max:
            max = list1[j + 1] - list1[j]
        j += 1
print(max)