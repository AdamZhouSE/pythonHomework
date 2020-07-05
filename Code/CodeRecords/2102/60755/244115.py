def prime(a, b):
    res = ""
    if a < 2:
        a = 2
    for i in range(a, b+1):
        if i == 2:
            res = res + str(i) + " "
        else:
            flag = 0
            for k in range(2, i-1):
                if i % k == 0:
                    flag = 1
                    break
            if flag == 0:
                res = res + str(i) + " "
    return res


num = int(input())
res = prime(2,num).split(" ")
print(len(res)-1)
                       