list1 = input().split(",")
list1 = [int(i) for i in list1]
list1.sort()
target = int(input())
if list1.count(target):
    print(list1.index(target))
else:
    list1.append(target)
    list1.sort()
    print(list1.index(target))