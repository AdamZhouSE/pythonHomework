
import math
def isPow(n: int) -> bool:
    cnt = 0
    while True :
        if math.pow(3, cnt) == n :
            return True
        elif math.pow(3, cnt) < n :
            cnt += 1
            continue
        else:
            return False

n = int(input())
print(isPow(n))
