list1 = input().split(",")
list1 = [int(i) for i in list1]
list1.sort()
print(list1[len(list1) - 1] * list1[len(list1) - 2] * list1[len(list1) - 3])