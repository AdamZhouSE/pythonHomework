
time=int(input())
result=[]
while time>0:
    exp=input()
    bracket=[]
    for token in exp:
        if token=='(' or token==')':
            bracket.append(token)
    counter1=0
    for item in bracket:
        if '(' not in bracket:
            break
        if item=='(':
            counter1=counter1+1
            bracket[bracket.index(item)]=counter1
    table=[i for i in range(1,counter1+1)]
    counter2=0
    for i in bracket:
        if type(i)==int:
            counter2=i
            continue
        else:
            bracket[bracket.index(i)]=counter2
            table.remove(counter2)
                #counter2=从后向前最近一个没有匹配的括号数
            for single in table:
                if single<counter2:
                    target=single
                else:
                    break
            counter2=target

    result.append(bracket)

    time=time-1

for res in result:
    print(' '.join(str(c) for c in res)+' ')

