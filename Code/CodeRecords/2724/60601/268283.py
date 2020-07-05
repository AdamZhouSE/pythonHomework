n = eval(input())
for i in range(n):
    a = eval(input())
    re = 0
    if a == 1:
        re = 6
    elif a == 2:
        re = 5
    elif a == 3:
        re = 4
    elif a == 4:
        re = 3
    elif a == 5:
        re = 2
    elif a == 6:
        re = 1
    print(re)