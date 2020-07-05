def work(group,ls):#group：选在开始选的组数，ls：已经选的人
    if group==N+1:
        for i in range(len(ls)):
            result.append(ls[i])
        return True
    first=2*group-1
    second=2*group
    first_can=True
    second_can=True
    for i in range(len(ls)):
        if contra.__contains__([ls[i],first]) or contra.__contains__([first,ls[i]]):
            first_can=False
        if contra.__contains__([ls[i], second]) or contra.__contains__([second, ls[i]]):
            second_can=False
        if not first_can and not second_can:
            break
    if first_can:
        ifcan=work(group+1,ls+[first])
        if ifcan:
            return True
        else:
            if second_can:
                ifcan=work(group+1,ls+[second])
                if ifcan:
                    return True
                else:
                    return False
            else:
                return False
    elif second_can:
        ifcan=work(group+1,ls+[second])
        if ifcan:
            return True
        else:
            return False
    else:
        return False


nums=input().split(" ")
N=int(nums[0])
M=int(nums[1])
contra=[]
for i in range(M):
    contra.append(input().split(" "))
    contra[i][0]=int(contra[i][0])
    contra[i][1]=int(contra[i][1])

result=[]
ifcan=work(2,[1])#第一组选第一个
if ifcan:
    for i in range(len(result)):
        print(result[i])
else:
    ifcan=work(2,[2])
    if ifcan:
        for i in range(len(result)):
            print(result[i])
    else:
        print("NIE")


