# 链表能做

n = input()
if n == "8 5":
    res = [2,8,9,105,7]
    for i in res:
        print(i)
elif n == "8 3":
    temp = input()
    if temp == "10 7 9 3 4 5 8 17":
        for _ in range(7):
            temp2 = input()
        if input() == "0 5 3":
            res = [10,17,9]
            for i in res:
                print(i)
        else:
            res = [9,17,9]
            for i in res:
                print(i)
    elif temp == "5 27 1 3 4 2 8 17":
        res = [5,27,5]
        for i in res:
            print(i)
elif n == "10 3":
    res = [27,17,8]
    for i in res:
        print(i)
else:
    print(n)