testnum = int(input())
answerlist = list()
for i in range(testnum):
    num = int(input())
    str = input().split(' ')
    lists = [int(i) for i in str]
    finishlist = list()
    check = True
    while len(lists)>0:
        temp=0
        if check:
            temp = lists.pop()
            check=False
        else:
            temp = lists.pop(0)
            check=True
        lists.append(temp)
    alist = [str(i) for i in lists]
    strs = ' '.join(alist)
    answerlist.append(strs)
for i in range(len(answerlist)):
    print(answerlist[i])