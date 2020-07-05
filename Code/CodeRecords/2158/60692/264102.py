list1 = list(input().strip())
res = []
if list1[0] != '-' and not list1[0].isdigit():
    print(0)
else:
    if list1[0] == '-':
        for i in list1[1:]:
            if i.isdigit():
                res.append(i)
            else:
                break
        if int("".join(res)) > 2 ** 31:
            print(- 2 ** 31)
        else:
            print(- int("".join(res)))
    else:
        for i in list1:
            if i.isdigit():
                res.append(i)
            else:
                break
        if int("".join(res)) > 2 ** 31 - 1:
            print(2 ** 31 - 1)
        else:
            print(int("".join(res)))