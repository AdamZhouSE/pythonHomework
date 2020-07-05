nums = int(input())
list_all = []
for i in range(nums):
    length1, length2 = (int(x) for x in input().split(" "))
    list_temp = input().split(" ")
    for j in range(length1):
        list_temp[j] = int(list_temp[j])
    list_all.append(list_temp)
    list_temp2 = input().split(" ")
    for j in range(length2):
        list_temp2[j] = int(list_temp2[j])
    list_all.append(list_temp2)
for i in range(nums):
    list_temp1 = list_all[i * 2]
    list_temp2 = list_all[i * 2 + 1]
    list_temp1.extend(list_temp2)
    list_temp1.sort()
    for j in range(len(list_temp1)):
        print(list_temp1[j],end=" ")
    print()

