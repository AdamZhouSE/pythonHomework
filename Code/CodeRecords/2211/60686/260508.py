n, m = (int(i) for i in input().split(" "))
list_letter = []
list_num = []
list_research = []
for i in range(n):
    list_temp = input().split(" ")
    list_letter.append(list_temp[0])
    list_num.append(int(list_temp[1]))
list_name = [list_letter[0]]
for i in range(1, n):
    if i == list_num[i]:
        temp = (list_letter[i] + list_name[i - 1])
        list_name.append(temp)
    else:
        temp_father = list_num.index(list_num[i] - 1)
        temp = (list_letter[i] + list_name[temp_father])
        list_name.append(temp)
for i in range(m):
    list_research.append(input())
for i in range(m):
    count = 0
    for j in range(len(list_name)):
        if list_research[i] == list_name[j][0:len(list_research[i])]:
            count += 1
            continue
        else:
            continue
    print(count)
