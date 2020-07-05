list1 = []
for i in range(num):
    list1.append(input().split(" "))
list2 = list1[:]
dict = {}
dict1 = {}
for i in range(len(list1)):
    if not dict.get(list1[i][0], None):
        dict[list1[i][0]] = int(list1[i][1])
    else:
        dict[list1[i][0]] += int(list1[i][1])
max_num = max(dict.values())
winner = ''
for j in range(len(list2)):
    if not dict1.get(list2[j][0], None):
        dict1[list2[j][0]] = int(list2[j][1])
    else:
        dict1[list2[j][0]] += int(list2[j][1])
    if dict1.get(list2[j][0]) == max_num and dict.get(list2[j][0]) == max_num:
        winner = list2[j][0]
        break
print(winner)