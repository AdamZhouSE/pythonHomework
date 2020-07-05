import math
test_num = int(input())
for i in range(test_num):
    result = 0
    num = int(input())
    while num >1:
        height = math.floor(math.log(num,2))
        num -= pow(2,height)
        result +=1
    if num == 1:
        result +=1
    print(result)
