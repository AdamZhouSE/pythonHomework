import math
def func8():
    n, res, temp = int(input()), 0, 2
    while temp < n:
        i = int(math.sqrt(temp))
        flag = True
        for j in range(2,i+1):
            if temp%j == 0:
                flag = False
                break
        if flag:
            res += 1
        temp += 1
    print(res)
    return
func8()