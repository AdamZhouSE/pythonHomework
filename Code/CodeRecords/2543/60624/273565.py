def func27():
    t = int(input())
    while t > 0:
        t -= 1
        n = int(input())
        a = list(map(int, input().strip().split(" ")))
        size = 2
        res = [max(a)]
        while n - size >= 0:
            Min = 0
            for i in range(0, n - size+1):
                Min = max(Min, min(a[i:size + i]))
            res.append(Min)
            size += 1
        res[n-1] = min(a)
        for i in range(0,n-1):
            print(res[i],end=" ")
        print(res[n-1])
    return
func27()
