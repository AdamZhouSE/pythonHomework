list1 = input().split(",")
list1 = [int(i) for i in list1]
list1.sort()
i = 0
j = 1
while i < len(list1) - 1:
    j = i + 1
    if list1[j] - list1[i] > 1:
        print(list1[i] + 1)
        break
    i += 1