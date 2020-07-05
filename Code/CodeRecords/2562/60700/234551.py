testNum = input()
num = []
opCodes = []
for i in range(int(testNum)):
    num.append(input())
    opCodes.append(input())

for i in range(int(testNum)):
    Num = num[i].split(' ')  # Num列表包括当前用例的邮件数和操作码数
    OpCodes = opCodes[i].split(' ')  # OpCodes列表包括当前用例的所有操作码
    unread = []
    for j in range(int(Num[0])):  # 初始化Unread列表
        unread.append(str(j+1))
    read = []
    trash = []
    p = 0  # 操作码列表的指针，初始指向0
    for k in range(int(Num[1])):
        if OpCodes[p] == '1':
            p += 1
            unread.remove(OpCodes[p])
            read.append(OpCodes[p])
            p += 1
        elif OpCodes[p] == '2':
            p += 1
            read.remove(OpCodes[p])
            trash.append(OpCodes[p])
            p += 1
        elif OpCodes[p] == '3':
            p += 1
            unread.remove(OpCodes[p])
            trash.append(OpCodes[p])
            p += 1
        elif OpCodes[p] == '4':
            p += 1
            trash.remove(OpCodes[p])
            read.append(OpCodes[p])
            p += 1
        else:
            print("ERROR: invalid option code")
    for email in unread:
        print(email + ' ', end='')
    print()
    for email in read:
        print(email+' ', end='')
    print()
    for email in trash:
        print(email+' ', end='')
    print()