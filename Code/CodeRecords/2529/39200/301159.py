i = input()
A = list(i)
flag = 0
if int(i) == 1:
    print("true")
else:
    num = 1
    while len(str(num)) < len(A):
        num *= 2
    while len(str(num)) == len(A):
        B = list(str(num))
        C = A.copy()
        flag = 1
        for aNum in B:
            if aNum in C:
                C.remove(aNum)
            else:
                flag = 0
        if flag:
            print("true")
            break
        else:
            num *= 2

    if flag == 0:
        print("false")
