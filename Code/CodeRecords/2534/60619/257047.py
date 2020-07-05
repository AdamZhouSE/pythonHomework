def merge(list1, list2):
    list1.append(999999)
    list2.append(999999)
    i = 0
    j = 0
    final = []
    while i < len(list1) - 1 or j < len(list2) - 1:
        if list1[i] < list2[j]:
            final.append(list1[i])
            i += 1
        else:
            final.append(list2[j])
            j += 1
    return final


ori = eval(input())
result = ori[0]
if len(ori) > 1:
    for k in range(1, len(ori)):
        result = merge(result, ori[k])
print(result)
