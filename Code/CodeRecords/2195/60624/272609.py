def func6():
    T = int(input())
    while T > 0:
        T -= 1
        li = list(map(int, input().strip().split(" ")))
        left = li[0]
        right = li[1]
        res = 0
        for i in range(left, right + 1):
            temp = 0
            j = i
            while j != 0:
                if j % 2 == 1:
                    temp += 1
                j //= 2
            if temp == 2 or temp == 3 or temp == 5 or temp == 7:
                res += 1
        print(res)
    return
func6()