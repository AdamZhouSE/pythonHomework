t = int(input())
for i in range(t):
    str1 = input().split(" ")
    len1 = int(str1[0])
    len2 = int(str1[1])
    k = int(str1[2])
    listNum = (input() + " " + input()).split(" ")
    index = 0
    while index < k:
        for j in range(len(listNum)-index-1):
            if int(listNum[j]) < int(listNum[j+1]):
                temp = listNum[j+1]
                listNum[j+1] = listNum[j]
                listNum[j] = temp
        index += 1
    print(listNum[len(listNum)-k])