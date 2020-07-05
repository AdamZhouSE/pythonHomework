list0=input().split(',')
list0=[int(list0[i]) for i in range(len(list0))]
isF=False
if len(list0)>=3:
    for i in range(len(list0)):
        for j in range(i+2,len(list0)):
            if list0[i]>list0[j]:
                print('False')
                isF=True
                break
    if not isF:
        print('True')
else:
    print('True')
