list1=list(input())
list2=[]
isF=True
for index in list1:
    if index=='(':
        list2.append(index)
    if index==')':
        if len(list2)<1:
            print('NO',end='')
            isF=False
            break
        else:
            list2.pop()
if isF:
    if len(list2)==0:
        print('YES',end='')
    else:
        print('NO',end='')
    