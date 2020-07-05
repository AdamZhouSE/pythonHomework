num = input()
if int(num) > 0:
    lists = list(num)
    lists.reverse()
    str = ""
    for i in range(lists.__len__()):
        str += lists[i]
    print(num == str)
else:
    temp = -int(num)
    num = str(temp)
    lists = list(num)
    lists.reverse()
    str = ""
    for i in range(lists.__len__()):
        str += lists[i]
    print(num == str)