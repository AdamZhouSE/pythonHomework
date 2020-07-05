nums = int(input())
list_all = []
for i in range(nums):
    num = int(input())
    list1 = input().split(" ")
    list2 = input().split(" ")
    list3 = input().split(" ")
    for j in range(num):
        list1[j] = int(list1[j])
        list2[j] = int(list2[j])
        list3[j] = int(list3[j])
    list_all.append(list1)
    list_all.append(list2)
    list_all.append(list3)
for i in range(nums):
    list1 = list_all[i * 3]
    list2 = list_all[i * 3 + 1]
    list3 = list_all[i * 3 + 2]
    count = 0
    for j in range(0, len(list1)):
        for k in range(0, len(list3)):
            if list1[j] == list2[j] + list3[k]:
                count += 1
    print(count)
