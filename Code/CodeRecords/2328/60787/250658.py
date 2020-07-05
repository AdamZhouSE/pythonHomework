num=[int(i) for i in input().split(",")]
unfinished=True
if 2 in num:    #第二位0-3 第三位0-5 第四位任意
    while True:
        test=num
        re=[2]
        test.remove(2)
        if 3 in test:
            re.append(3)
            test.remove(3)
        elif 2 in test:
            re.append(2)
            test.remove(2)
        elif 1 in test:
            re.append(1)
            test.remove(1)
        elif 0 in test:
            re.append(0)
            test.remove(0)
        else:
            break
        if 5 in test:
            re.append(5)
            test.remove(5)
        elif 4 in test:
            re.append(4)
            test.remove(4)
        elif 3 in test:
            re.append(3)
            test.remove(3)
        elif 2 in test:
            re.append(2)
            test.remove(2)
        elif 1 in test:
            re.append(1)
            test.remove(1)
        elif 0 in test:
            re.append(0)
            test.remove(0)
        else:
            break
        re.append(test[0])
        unfinished=False
        break
if unfinished and (1 in num or 0 in num):    #第三位0-5 其他任意
    test=num
    if 1 in test:
        re=[1]
        test.remove(1)
    else:
        re=[0]
        test.remove(0)
    if max(test)>5:
        re.append(max(test))
        test.remove(max(test))
        if 5 in test:
            re.append(5)
            test.remove(5)
            re.append(test[0])
            unfinished=True
        elif 4 in test:
            re.append(4)
            test.remove(4)
            re.append(test[0])
            unfinished = True
        elif 3 in test:
            re.append(3)
            test.remove(3)
            re.append(test[0])
            unfinished = True
        elif 2 in test:
            re.append(2)
            test.remove(2)
            re.append(test[0])
            unfinished = True
        elif 1 in test:
            re.append(1)
            test.remove(1)
            re.append(test[0])
            unfinished = True
        elif 0 in test:
            re.append(0)
            test.remove(0)
            re.append(test[0])
            unfinished = True
    else:
        test=sorted(test)
        test.reverse()
        re=re+test
        unfinished=True
if unfinished:
    print("")
else:
    re=[str(i) for i in re]
    print(re[0]+re[1]+":"+re[2]+re[3])