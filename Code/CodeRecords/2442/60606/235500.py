import math
array = input()
result = array[1:len(array)-1].split(",")
result = [int(x) for x in result]
result.sort()
if len(result) > 2:
    max = math.fabs(result[0] - result[1])
    for i in range(1,len(result)):
        if math.fabs(result[i] - result[i-1]) > max:
            max = math.fabs(result[i] - result[i-1])
    print(int(max))
else:
    print(0)
