import math
def exploit(num,factor):
    temp = num
    while math.floor(temp/factor) == temp/factor:
        temp/=factor
    return temp

n = int(input())
result = [1]
for i in range(2,1000):
    temp = i
    temp = exploit(temp,2)
    temp = exploit(temp, 3)
    temp = exploit(temp, 5)
    if temp == 1:
        result.append(i)
print(result[n-1])