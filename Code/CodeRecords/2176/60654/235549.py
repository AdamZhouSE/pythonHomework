s = input()
list1 = []
list3 = {}
result = ""
for i in range(s.__len__()):
    list1.append(s[i: s.__len__()])
    list3[s[i: s.__len__()]] = i+1
list1.sort()
for i in list1:
    result += str(list3[i])
    if i!=list1[-1]:
        result += " "
print(result)