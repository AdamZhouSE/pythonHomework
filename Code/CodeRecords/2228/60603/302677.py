import math
def reachNumber(target):    
    target = abs(target)
    n = math.sqrt(2 * target + 0.25) - 0.5;
    n = int(n)
    sum = (n * n + n) / 2
    while (sum < target or (sum - target) % 2 != 0):
        n = n + 1
        sum = sum + n
    print(n)
target=abs(int(input()))
reachNumber(target)