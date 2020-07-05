strs = input()
index = -1
lists = list(strs)
#print(lists)
check_1 = True
check_2 = True
check_0 = True
while len(lists)>0:
    print(lists)
    if lists[0]!='2':
        print('break')
        check_1 = False
        check_2 = False
        check_0 = True
        break
#    assert lists[0]=='2'
    try:
        indexs = lists.index('5')
    except:
        print('break')
        check_1 = False
        check_2 = False
        check_0 = True
        break
    lists.pop(0)
    lists.pop(indexs-1)
    print("pop:{} & {}".format(0,indexs))
    if indexs==1 and check_1:
        check_1 = True
        check_2 = False
        check_0 = False
    else:
        check_1 = False
        check_2 = True
        check_0 = False
if check_1:print(1)
elif check_2:print(2)
else: print(-1)