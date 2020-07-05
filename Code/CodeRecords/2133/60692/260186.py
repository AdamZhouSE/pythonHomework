list1 = input().split(",")
list1 = [int(i) for i in list1]
list1.sort()
count = 0
while list1[len(list1) - 1] != list1[0]:
    list1 = [i + 1 for i in list1]
    list1[len(list1) - 1] -= 1
    count += 1
    list1.sort()
print(count)