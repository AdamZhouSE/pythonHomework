cases=[]
count=0#只有前两个操作增加cases
for i in range(int(input())):
    operation=input().split()
    if operation[0]=='T':
        if cases!=[]:
            cases.append(cases[count-1]+[operation[1]])
            count+=1
        else:
            cases.append([operation[1]])
            count+=1
    elif operation[0]=='U':
        cases.append(cases[count-1-int(operation[1])])
        count+=1
    else:
        print(cases[count-1][int(operation[1])-1])