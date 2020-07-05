import ast
lists = ast.literal_eval(input())
lists.sort()

flag = False
for i in range(lists.__len__()):
    if lists[i] < 0:
        flag = True
    else:
        flag = False

if flag:
    print(1)
else:
    index = 0
    flag = False
    for i in range(lists.__len__()):
        if lists[lists.__len__()-1-i] < 0:
            index = lists.__len__()-1-i
            flag = True
            break
    if flag:
        lists = lists[index+1:lists.__len__()]
    else:
        lists = lists[index:lists.__len__()]
    #print(lists)
    base = []
    for i in range(lists[0], lists[lists.__len__()-1]+1):
        base.append(i)
    '''print("base: ", end="")
    print(base)
    print("lists: ", end="")
    print(lists)'''
    set1 = set(lists)
    set2 = set(base)
    '''print("set1: ", end="")
    print(set1)
    print("set2: ", end="")
    print(set2)'''
    if set1 == set2:
        lists1 = list(set1)
        print(max(lists1)+1)
    else:
        set3 = set2.difference(set1)
        minNum = min(set3)
        print(minNum)
