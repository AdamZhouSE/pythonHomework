def func4():
    t = int(input())
    while t>0:
        t -= 1
        n = int(input())
        temp = n
        res = ""
        while temp > 0:
            res += str(temp)+" "
            temp -= 5
        while temp != n:
            res += str(temp)+" "
            temp += 5
        res += str(n)+" "
        print(res)
    return
func4()