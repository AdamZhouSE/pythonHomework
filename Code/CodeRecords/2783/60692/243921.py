num = int(input())
list1 = []
for i in range(num):
    list1.append(input().split(" "))
for m in range(len(list1)):
    for n in range(m + 1, len(list1)):
        if list1[m][0] == list1[n][0]:
            list1[n][1] = str(int(list1[m][1])+int(list1[n][1]))
winner = list1[0][0]
max_num = int(list1[0][1])
for j in range(1, len(list1)):
    if int(list1[j][1]) > max_num:
        winner = list1[j][0]
        max_num = int(list1[j][1])
print(winner)