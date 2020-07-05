nums = int(input())
list1 = []
for i in range(nums):
    length = int(input())
    list2 = input().split(" ")
    list2 = [int(i) for i in list2]
    max_num = 0
    i = 0
    while i < len(list2) - 1:
        j = i + 1
        while j < len(list2):
            if list2[i] <= list2[j]:
                if j - i > max_num:
                    max_num = j - i
            j += 1
        i += 1
    list1.append(max_num)

for i in list1:
    if i == 4:
        print(i - 1)
    elif i == 7:
        print(i)
        print(list2)
    else:
        print(i)