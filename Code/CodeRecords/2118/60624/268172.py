def func14():
    n = int(input())
    flag = True
    if n<1:
        flag = False
    while n>1:
        if n%3 != 0:
            flag = False
            break
        n //= 3
    print(flag)
    return
func14()