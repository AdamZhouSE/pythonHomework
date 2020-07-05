strs = input()
index = -1
lists = list(strs)
check_1 = True
check_2 = True
check_0 = True
while len(lists)>0:
    if lists[0]!='2':
        check_1 = False
        check_2 = False
        break
#    assert lists[0]=='2'
    index = lists.index('5')
    if index==1 and check_1:
        check_1 = True
        check_2 = False
    else:
        check_1 = False
        check_2 = True
if check_1:print(1)
elif check_2:print(2)
else: print(-1)