ori = input()
listNum = ori[1:len(ori)-1].split(",")
list2 = []
for i in range(len(listNum)):
    list2.append(int(listNum[i]))
k = len(list2)
while k > 1:
    for j in range(k-1):
        if list2[j] > list2[j+1]:
            temp = list2[j+1]
            list2[j+1] = list2[j]
            list2[j] = temp
    k -= 1
print(list2)