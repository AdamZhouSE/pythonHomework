num = int(input())
for j in range(num):
    arr = list(input())
    res = 0
    get = 0
    for i in arr:
        if "{" == i:
            get += 1
        elif "}" == i:
            if get > 0:
                get -= 1
            else:
                res += 1
                get += 1
    if get % 2 == 0:
        res+=get//2
    else:
        res = -1
    print(res)