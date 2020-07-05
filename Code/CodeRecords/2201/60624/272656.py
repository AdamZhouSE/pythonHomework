import math
def func8():
    t = int(input())
    def is_prime(n:int)->bool:
        temp = int(math.sqrt(n))
        for j in range(2,temp+1):
            if n%j == 0:
                return False
        return True
    while t>0:
        pens = list(map(int, input().strip().split(" ")))
        i = 1
        while True:
            if is_prime(pens[0]+pens[1]+i):
                print(i)
                break
            i += 1
    return
func8()