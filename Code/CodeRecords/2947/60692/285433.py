n = int(input())
str1 = input()
res = []
for i in range(n):
    command = input().split(" ")
    if int(command[0]) == 1:
        str1 += command[1]
        res.append(str1)
    elif int(command[0]) == 2:
        str1 = str1[int(command[1]): int(command[1]) + int(command[2])]
        res.append(str1)
    elif int(command[0]) == 3:
        str1 = str1[0: int(command[1])] + command[2] + str1[int(command[1]):]
        res.append(str1)
    elif int(command[0]) == 4:
        if str1.index(command[1]):
            res.append(str1.index(command[1]))
        else:
            res.append(-1)
for j in res:
    print(j)