data = input()
op= input()
if op[0]=='D':
    flag = 0
    for i in data:
        if flag == 0 and i == op[3]:
            print('',end='')
            flag=1
        else:
            print(i,end='')
    print()
elif op[0]=='I':
    flag = 0
    li=[]
    leng=len(data)
    for i in range(0,len(data)):
        if flag == 0 and data[leng-1-i]==op[3]:
            li.append(data[leng-i-1])
            li.append(op[5])
            flag=1
        else:
            li.append(data[leng-i-1])
    print(''.join(reversed(li)),end='')
    print()
elif op[0]=='R':
    if op[4] not in data:
        print('no exist')
        print(data)
    else:
        for i in data:
            if(i==op[3]):
                print(op[5],end='')
            else:
                print(i,end='')
        print()
                