a = input().lstrip("[").rstrip("]")
b = input().lstrip("[").rstrip("]")
list1 = a.split(",")
list2 = b.split(",")
list1.sort()
list2.sort()
list3 = []
for num in list1:
    if list2.__contains__(num) and (not list3.__contains__(num)):
        list3.append(num)
print([int(x) for x in list3])