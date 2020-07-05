list1 = input().split(",")
list1 = [int(i) for i in list1]
list1.sort()
B = []
C = []
average = sum(list1) / len(list1)
i = 0
j = len(list1) - 1
while i < j:
    if list1[i] == average:
        i += 1
        B.append(list1[i])
        break
    elif list1[j] == average:
        j -= 1
        B.append(list1[j])
        break
    else:
        if (list1[i] + list1[j]) / 2 == average:
            B.append(list1[i])
            B.append(list1[j])
            break
        elif (list1[i] + list1[j]) / 2 > average:
            j -= 1
        else:
            i += 1
if B:
    print(True)
else:
    print(False)