import math
s = int(input())
array = input().split(",")
array = [int(x) for x in array]
temp = array[0]
length = 1
sentinel = 0
result = []
for i in range(len(array)):
    if array[i] == s:
        print(1)
        sentinel = 2
        break
if sentinel != 2:
    for i in range(1, len(array)):
        if math.fabs(array[i] - array[i - 1]) == 1 or math.fabs(array[i] - array[i - 1]) == 0:
            temp += array[i]
            length += 1
            if temp >= s:
                sentinel = 1
                result.append(length)
                length = 0
                temp = 0
        else:
            temp = array[i]
            length = 1
min = 99
if sentinel == 1:
    for i in result:
       if min >i:
           min = i
    print(min)
if sentinel == 0:
    print(0)
