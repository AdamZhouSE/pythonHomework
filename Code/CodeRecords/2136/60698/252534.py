a = int(input())
k = 2
check_flag = False
while True:
    e = 0
    check = 0
    while True:
        check = check + pow(k, e)
        if a == check:
            check_flag = True
            break
        elif a > check:
            e = e + 1
        else:
            k = k + 1
            break
    if check_flag:
        break
print(k)