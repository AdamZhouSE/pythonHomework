list1 = input()
list2 = input()
list1 = list1[1:len(list1) - 1].split(",")
list2 = list2[1:len(list2) - 1].split(",")
for i in range(len(list2)):
    list2[i] = int(list2[i])
for i in range(len(list1)):
    list1[i] = int(list1[i])
list1.sort()
list2.sort()
res = []
if len(list2) > len(list1):
    flag = False
    length = len(list1)
else:
    flag = True
    length = len(list2)
for i in range(0, length):
    if flag:
        if list1.count(list2[i]) > 0 and res.count(list2[i]) == 0:
            res.append(list2[i])
    else:
        if list2.count(list1[i]) > 0 and res.count(list1[i]) == 0:
            res.append(list1[i])
print(res)
