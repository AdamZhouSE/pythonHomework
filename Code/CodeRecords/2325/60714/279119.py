nums = eval(input())
if nums == 1:
    print(False)
else:
    temp = dict()
    for item in nums:
        if item in temp:
            temp[item] += 1
        else:
            temp[item] = 1
    pos = min(temp.values())
    flag = True
    if pos == 1:
        flag = False
    else:
        for item in temp.values():
            if item % pos != 0:
                flag = False
                break
    print(flag)
