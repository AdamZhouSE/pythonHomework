nums = int(input())
list1 = []
for i in range(nums):
    length = int(input())
    list2 = input().split(" ")
    list2 = [int(i) for i in list2]
    list3 = []
    max_num = 0
    i = 0
    j = 1
    while i < len(list2) and j < len(list2):
        if list2[j] > list2[j - 1]:
            max_num = list2[j] - list2[i]
            if j == len(list2) - 1 and j - i > 1:
                list3.append("("+str(i)+" "+str(j)+")")
            j += 1
        elif list2[j] <= list2[j - 1] or j == len(list2) - 1:
            if j - i > 1:
                list3.append("("+str(i)+" "+str(j - 1)+")")
            i = j
            j = i + 1
    if not list3:
        list1.append("没有盈利")
    else:
        list1.append(" ".join(list3))

for i in list1:
    print(i)