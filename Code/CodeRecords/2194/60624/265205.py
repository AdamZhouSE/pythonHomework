import math
def func5():
    t = int(input())
    while t>0:
        t -= 1
        temp = list(map(int, input().split(" ")))
        m = temp[0]
        n = temp[1]
        res = ""
        def is_prime(n:int)->bool:
            if n == 1:
                return False
            a = int(math.sqrt(n))
            for i in range(2, a+1, 1):
                if n%i == 0:
                    return False
            return True
        for i in range(m, n+1, 1):
            if is_prime(i):
                res += str(i)+" "
        print(res[:-1])
    return
func5()