str = input()
lists = list(str)

suffix = []
for i in range(lists.__len__()):
    temp = lists[i: lists.__len__()]
    s = ""
    for j in range(temp.__len__()):
        temp1 = []
        s += temp[j]
        temp1.append(s)
        temp1.append(i+1)
    suffix.append(temp1)
#print(suffix)
suffix.sort()
#print(suffix)
for i in range(suffix.__len__()):
    if i == suffix.__len__()-1:
        print(suffix[i][1])
    else:
        print(suffix[i][1], end=" ")
