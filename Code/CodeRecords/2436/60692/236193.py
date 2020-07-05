a = input()
b = input()
list0 = []
list1 = []
list2 = b.split(",")
list3 = []
i = 0
while i < len(a):
    if a[i].isdigit() and a[i+1].isdigit():
        list0.append(int(a[i]+a[i+1]))
        i = i + 1
    elif a[i].isdigit():
        list0.append(int(a[i]))
    i = i + 1
for i in range(0, len(list0), 2):
    list1.append([list0[i], list0[i+1]])

list2.insert(1, list2[0][1:])
list2.remove(list2[0])
list2.insert(-1, list2[-1][0:-1])
list2.remove(list2[-1])

for j in range(len(list2)):
    list2[j] = int(list2[j])
p = 0
q = len(list1) - 1
pos = 0
while p < q:
    mid = (p + q) // 2
    if list1[mid][0] <= int(list2[0]):
        p = mid + 1
    elif int(list2[1]) <= list1[mid][1]:
        q = mid
pos = p
list1.insert(pos, list2)
for i in range(0, len(list1)):
    for j in range(i+1, len(list1)):
        if list1[j][1] >= list1[i][1] >= list1[j][0] > list1[i][0]:
            list1[i][1] = list1[j][1]
            list1[j][0] = list1[i][0]
        elif list1[j][0] <= list1[i][0] <= list1[j][1] < list1[i][1]:
            list1[i][0] = list1[j][0]
            list1[j][1] = list1[i][1]
        elif list1[i][0] == list1[j][0] and list1[j][1] == list1[i][1]:
            j = j
        elif list1[i][0] <= list1[j][0] and list1[i][1] >= list1[j][1]:
            list1[j][0] = list1[i][0]
            list1[j][1] = list1[i][1]
        elif list1[j][0] <= list1[i][0] and list1[i][1] <= list1[j][1]:
            list1[i][0] = list1[j][0]
            list1[i][1] = list1[j][1]
    if list3.count(list1[i]) == 0:
        list3.append(list1[i])
print(list3)