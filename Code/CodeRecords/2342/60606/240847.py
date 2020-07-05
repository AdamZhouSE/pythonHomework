import math
test_num = int(input())
for i in range(test_num):
    line1 = input().split(" ")
    line2 = input().split(" ")
    n = int(line1[0])
    k = int(line1[1])
    result = []
    time = math.floor(len(line2) / k)
    for j in range(1,time+1):
        target = line2[(j-1)*k:j*k]
        target.reverse()
        result += target
    if len(result) != len(line2):
        short = len(line2) - len(result)
        target = line2[len(line2) - short:]
        target.reverse()
        result += target
    for k in result:
        print(k,end=" ")
    print()
