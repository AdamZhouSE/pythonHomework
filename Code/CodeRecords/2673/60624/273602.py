def func28():
    t = int(input())
    while t > 0:
        t -= 1
        g = int(input())
        li = []
        while g > 0:
            if g%2 == 0:
                li.append(0)
            else:
                li.append(1)
            g //= 2
        res = [li[len(li) - 1]]
        i = len(li)-2
        j = 0
        while i >= 0:
            if li[i] != res[j]:
                res.append(1)
            else:
                res.append(0)
            i -= 1
            j += 1
        size = len(res)
        j = 0
        for i in range(0,len(res)):
            if res[i] == 1:
                j += pow(2,size-i-1)
        print(j)
    return
func28()