arr = list(input().split(","))
list1 = []
sign = True
for i in arr:
    if list1.__len__() == 0:
        list1.append(int(i))
    for j in list1:
        if j%int(i) != 0 and int(i) % j !=0:
            sign = False
            break
    if sign and not list1.count(int(i)):
        list1.append(int(i))
print(list1)