list1 = input()[1:-1].split(",")
list1 = [int(i) for i in list1]
list1.sort()
list1.reverse()
print(list1)