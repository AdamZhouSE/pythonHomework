num = int(input())
if num >0:
    str = str(num)
    lists = list(str)
    lists.reverse()
    res = ""
    for i in range(lists.__len__()):
        res += lists[i]
    print(res)
else:
    num = -num
    str = str(num)
    lists = list(str)
    lists.reverse()
    res = ""
    for i in range(lists.__len__()):
        res += lists[i]
    print("-"+res)