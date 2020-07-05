import math
def func2():
    n = input()
    s = list(map(int, input().strip().split(" ")))
    sum1 = s.count(1)
    sum2 = s.count(2)
    sum3 = s.count(3)
    sum4 = s.count(4)
    res = sum4
    if sum1 >= sum3:
        res += sum3 + sum2 // 2
        sum1 -= sum3
        sum2 %= 2
        if sum2 == 1:
            res += 1
            sum1 -= 2
        if sum1 > 0:
            res += math.ceil(sum1/4.0)
        print(res)
    else:
        res += sum3+math.ceil(sum2/2.0)
        print(res)
    return
func2()