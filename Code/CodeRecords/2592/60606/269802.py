import math
test_num = int(input())
for i in range(test_num):
    sum = 0
    R = int(input())
    for j in range(1,2*R):
        temp = 2*math.sqrt(R*R-j*j/4)
        sum += math.floor(temp)
    print(sum)
