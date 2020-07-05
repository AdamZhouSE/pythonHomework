size = int(input())
a = 0
while a < size:
    b = input()
    strList = input().split()
    i = 0
    while i < len(strList):
        l = list(strList[i])
        l.sort()
        s = "".join(l)
        strList[i] = s
        i = i + 1
    strList.sort()
    j = 0
    k = 1
    myList = []
    while j < len(strList):
        if j == len(strList) - 1:
            break
        if (strList[j] == strList[j + 1]):
            k = k + 1
        else:
            myList.append(k)
            k = 1
        j = j + 1
    myList.append(k)
    myList.sort()
    m = 0
    while m < len(myList):
        if m != len(myList) - 1:
            print(myList[m], end='')
            print(" ", end='')
        else:
            print(myList[m])
        m = m + 1
    a = a + 1