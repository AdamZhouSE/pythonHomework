list1 = input().split(" ")
m = int(list1[0])
n = int(list1[1])
oriString = input()
for i in range(n):
    listNum = input().split(" ")
    a = int(listNum[0])
    b = int(listNum[1])
    c = int(listNum[2])
    d = int(listNum[3])
    if b == m:
        str1 = oriString[a-1:]
    else:
        str1 = oriString[a-1:b]
    if d == m:
        str2 = oriString[c-1:]
    else:
        str2 = oriString[c-1:d]
    length = 0
    for j in range(min(len(str1),len(str2))):
        if str1[j] == str2[j]:
            length += 1
        else:
            break
    print(length)