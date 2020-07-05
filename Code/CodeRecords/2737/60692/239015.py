list1 = input()[1:-1].split(",")
can_a = 0
count_a = 0
can_b = 0
count_b = 0
le = len(list1) // 3
for i in list1:
    if can_a == int(i):
        count_a += 1
    elif can_b == int(i):
        count_b += 1
    elif count_a == 0:
        can_a = int(i)
        count_a += 1
    elif count_b == 0:
        can_b = int(i)
        count_b += 1
    else:
        count_a -= 1
        count_b -= 1
count_a = 0
count_b = 0
for j in list1:
    if int(j) == can_a:
        count_a += 1
    elif int(j) == can_b:
        count_b += 1
list1.clear()
if count_a >= le:
    list1.append(str(can_a))
if count_b >= le:
    list1.append(str(can_b))
for k in range(len(list1)):
    list1[k] = int(list1[k])
print(list1)