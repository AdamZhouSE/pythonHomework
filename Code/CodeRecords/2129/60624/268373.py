def func17():
    n = int(input())
    def helper(num:int)->int:
        if num == 1:
            return 1
        if n == 3:
            return 2
        if num%2 == 0:
            return num//2
        elif (num+1)%4 == 0:
            return num+1
        else:
            return num-1
    res = 0
    while True:
        n = helper(n)
        res += 1
        if n == 1:
            break
    print(res)
    return
func17()