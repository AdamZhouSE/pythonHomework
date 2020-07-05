list1 = input()[1:-1].split(",")
for i in range(len(list1)):
    list1[i] = int(list1[i])
list2 = list1[:]
list2.sort()
list3 = []
j = len(list2) - 1
while j > 0:
    max_one = list2[j]
    index = list1.index(max_one)
    if index < j:
        list3.append(index + 1)
        list3.append(j + 1)
        for k in range((index + 1) // 2):
            list1[k], list1[index - k] = list1[index - k], list1[k]
        for m in range((j + 1) // 2):
            list1[m], list1[j - m] = list1[j - m], list1[m]
    j -= 1
print(list3)
