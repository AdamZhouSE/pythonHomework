def reads(i):
    unread.remove(int(all_eg[2 * i + 1]))
    read.append(int(all_eg[2 * i + 1]))


def trashs(i):
    read.remove(int(all_eg[2 * i + 1]))
    trash.append(int(all_eg[2 * i + 1]))


def notlook(i):
    unread.remove(int(all_eg[2 * i + 1]))
    trash.append(int(all_eg[2 * i + 1]))


def restore(i):
    trash.remove(int(all_eg[2 * i + 1]))
    read.append(int(all_eg[2 * i + 1]))


NumOfEg = int(input())
result = []
while NumOfEg > 0:
    all_num = input().split(" ")
    all_eg = input().split(" ")
    unread = []
    read = []
    trash = []
    num1 = int(all_num[0])
    one = 1
    while one <= num1:
        unread.append(one)
        one = one + 1
    num2 = int(all_num[1])
    zero = 0
    while zero < num2:
        num3 = int(all_eg[2 * zero])
        if num3 == 1:
            reads(zero)
        elif num3 == 2:
            trashs(zero)
        elif num3 == 3:
            notlook(zero)
        elif num3 == 4:
            restore(zero)
        zero = zero + 1
    res = ""
    for x in unread:
        res = res + str(x) + " "
    if res == "":
        res = "EMPTY"
    result.append(res)
    res = ""
    for x in read:
        res = res + str(x) + " "
    if res == "":
        res = "EMPTY"
    result.append(res)
    res = ""
    for x in trash:
        res = res + str(x) + " "
    if res == "":
        res = "EMPTY"
    result.append(res)
    NumOfEg = NumOfEg-1
for x in result:
    print(x)
