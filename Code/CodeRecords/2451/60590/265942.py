lists = list(map(int, input().split(",")))
toFind = int(input())

isIn = lists.__contains__(toFind)
if isIn:
    print(lists.index(toFind))
else:
    arr = lists.copy()
    arr.append(toFind)
    arr.sort()
    #print(lists)
    #print(arr)
    res = 0
    index = 0
    flag = False
    while index != lists.__len__():
        if lists[index] != arr[index]:
            res = index
            flag = True
            break
        else:
            index += 1
    if not flag:
        res = arr.__len__()-1
    print(res)