list1 = input().split(" ")
m = int(list1[0])
n = int(list1[1])
oriString = input()
print(oriString)
for i in range(2):
    listNum = input().split(" ")
    end1 = int(listNum[0])
    print(end1)
    end2 = int(listNum[1])
    print(end2)
    if end1 == 1:
        str1 = oriString[0]
    else:
        str1 = oriString[:end1]
    if end2 == 1:
        str2 = oriString[0]
    else:
        str2 = oriString[:end2]
    length = 0
    x = len(str1)-1
    y = len(str2)-1
    while x >= 0 and y >= 0:
        if str1[x] == str2[y]:
            length +=1
        else:
            break
        x -= 1
        y -= 1
    print(length)