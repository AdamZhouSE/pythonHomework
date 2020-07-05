nums = int(input())
for j in range(nums):
    list1 = input().split(" ")
    for i in range(len(list1)):
        list1[i] = int(list1[i])
    list2 = input().split(" ")
    for i in range(len(list2)):
        list2[i] = int(list2[i])
    list3 = input().split(" ")
    for i in range(len(list3)):
        list3[i] = int(list3[i])
    list2.extend(list3)
    list2.sort()
    print(list2[list1[2] - 1])
