str = input()
list = []
for i in range(len(str)):
    if str[i] not in list:
        list.append(str[i])
for i in list:
    for j in range(len(str)):
        if i == str[j]:
            print(j+1,end= ' ')