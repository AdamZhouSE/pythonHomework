list0 = input().split(" ")
n = int(list0[0])
k = int(list0[1])
list1 = []
list_name = []
list2 = []
for i in range(n):
    strname = ""
    list1 = input().split(' ')
    if int(list1[1]) == 0:
        strname = list1[0]
        list_name.append(strname)
    else:
        strname += list1[0]
        strname += list_name[int(list1[1]) - 1]
        list_name.append(strname)
for j in range(k):
    list2.append(input())
for m in list2:
    count = 0
    for p in range(len(list_name)):
        if list_name[p][0:len(m)] == m:
            count += 1
    print(count)