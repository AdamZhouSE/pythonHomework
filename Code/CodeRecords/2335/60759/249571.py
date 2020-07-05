def getnum():
    x = int(input())
    y = int(input())
    if x >= y:
        return x - y
    lst = [y]
    lst_c = lst.copy()
    ans = 1
    while(True):
        temp = []
        for item in lst_c:
            temp.append(item + 1)
            if item % 2 == 0:
                temp.append(item // 2)
        if x in temp:
            return ans
        ans += 1
        lst_c = temp


print(getnum())
