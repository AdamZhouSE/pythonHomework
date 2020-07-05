num = int(input())
if num >0:
    str = str(num)
    lists = list(str)
    lists.reverse()
    index = 0
    for i in range(lists.__len__()):
        if lists[i] != '0':
            index = i
            break
    #print(index)
    lists = lists[index:lists.__len__()]
    res = ""
    for i in range(lists.__len__()):
        res += lists[i]
    print(res)
else:
    num = -num
    str = str(num)
    lists = list(str)
    lists.reverse()
    index = 0
    for i in range(lists.__len__()):
        if lists[i] != '0':
            index = i
            break
    # print(index)
    lists = lists[index:lists.__len__()]
    res = ""
    for i in range(lists.__len__()):
        res += lists[i]
    print("-"+res)