import math

test_num = int(input())
for i in range(test_num):
    num = 0
    n = int(input())
    while n != 1 and n != 0:
        height = math.floor(math.log(n, 2))
        n = n - (math.pow(2, height))
        num += 1
    if n == 1:
        num += 1
    print(num)
