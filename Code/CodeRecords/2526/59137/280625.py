def s1():
    list1 = input().split(',')
    list2 = input().split(',')
    flag1 = True
    flag2 = True

    if list1[0] == '[]':
        flag1 = False
    if list2[0] == '[]':
        flag2 = False

    list1[0] = list1[0][1:]
    list1[-1] = list1[-1][:-1]
    list2[0] = list2[0][1:]
    list2[-1] = list2[-1][:-1]

    answer = []

    if flag1:
        for x in list1:
            if x != 'null':
                answer.append(eval(x))
    if flag2:
        for x in list2:
            if x != 'null':
                answer.append(eval(x))

    answer = sorted(answer)
    print(answer)


s1()