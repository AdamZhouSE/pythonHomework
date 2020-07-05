def reverse(a:int):
    global lists
    templist = list()
    for t in range(a):
        templist.append(lists.pop(0))
    templist.reverse()
    templist.extend(lists)
    lists = templist

def operate_A(i:int):
    if i==min(lists):
        return
    temp = lists.index(i)
    if temp!=0:
        operas.append(temp)
        reverse(temp)
    operas.append(i)
    reverse(i)
    operate_A(i-1)

lists = list(eval(input()))
operas = list()
operate_A(max(lists))
print(operas)