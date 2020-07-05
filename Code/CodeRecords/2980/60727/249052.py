data = input()
op= input()
if op[0]=='D':
    flag = 0
    for i in data:
        if flag == 0 and i == op[2]:
            print('',end='')
            flag=1
        else:
            print(i,end='')
    print()
if op[0]=='l':
    flag = 0
    li=[]
    leng=len(data)
    for i in range(0,len(data)):
        if flag == 0 and data[leng-1-i]==op[1]:
            li.append(data[leng-i-1])
            li.append(op[2])
            flag=1
        else:
            li.append(data[leng-i-1])
    print(''.join(li.reverse()))
    print()