def operate(temp:list):
    alist = list()
    for i in range(len(temp)-1):
        if temp[i]<=temp[i+1]:
            alist.append(-1)
        else:
            alist.append(temp[i+1])
    else:
        alist.append(-1)
    strlist = [str(i) for i in alist]
    strlist.append('')
    pr = ' '.join(strlist)
    print(pr)
usecase = int(input())
numbercom = list()
for i in range(usecase):
    n = int(input())
    strs = input().split()
    lists = [int(k) for k in strs]
    numbercom.append(lists)
for i in range(usecase):
    operate(numbercom[i])