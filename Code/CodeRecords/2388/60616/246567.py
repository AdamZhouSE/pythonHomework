testNum=int(input())
for i in range (testNum):
    size=int(input())
    list1=input().split(' ')
    list2=input().split(' ')
    bo1 = True
    bo2 = True
    for item1 in list1:
        if (item1 not in list2):
            bo1 = False
            break
        else:
            if (list1.count(item1) != list2.count(item1)):
                bo1 = False
                break
    for item2 in list2:
        if (item2 not in list1):
            bo2 = False
            break
        else:
            if (list1.count(item2) != list2.count(item2)):
                break
    if(bo1 and bo2):print('1')
    else:print('0')