tests = int(input())

lists = []
for i in range(tests):
    temp = list(map(int, input().split()))
    lists.append(temp)

for i in range(lists.__len__()):
    ele = lists[i]
    num1 = ele[0]
    num2 = ele[1]
    str1 = bin(num1)
    str2 = bin(num2)
    length = max(str1.__len__(), str2.__len__())
    #print(length)
    while str1.__len__() < length:
        str1 = str1 +"2"
    while str2.__len__() < length:
        str2 = str2 +"2"
    '''print("str1: ", end="")
    print(str1)
    print("str2: ", end="")
    print(str2)'''
    list1 = list(str1)
    list2 = list(str2)
    if list1 == list2:
        print(-1)
    flag = 0
    for j in range(list1.__len__()):
        if list1[j] != list2[j]:
            flag = j
    print(flag-2)