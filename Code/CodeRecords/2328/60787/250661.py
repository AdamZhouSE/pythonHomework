num=[int(i) for i in input().split(",")]
unfinished=True
if 2 in num:    #第二位0-3 第三位0-5 第四位任意
    while True:
        test=list(num)
        re=[2]
        test.remove(2)
        for i in range(3,-1,-1):
            if i in test:
                re.append(i)
                test.remove(i)
                break
        else:
            break
        for i in range(5,-1,-1):
            if i in test:
                re.append(i)
                test.remove(i)
                break
        else:
            break
        re.append(test[0])
        unfinished=False
        break
if unfinished and (1 in num or 0 in num):    #第三位0-5 其他任意
    test=list(num)
    if 1 in test:
        re=[1]
        test.remove(1)
    else:
        re=[0]
        test.remove(0)
    if max(test)>5:
        re.append(max(test))
        test.remove(max(test))
        for i in range(5,-1,-1):
            if i in test:
                re.append(i)
                test.remove(i)
                re.append(test[0])
                unfinished=False
    else:
        test=sorted(test)
        test.reverse()
        re=re+test
        unfinished=False
if unfinished:
    print("")
else:
    re=[str(i) for i in re]
    print(re[0]+re[1]+":"+re[2]+re[3])