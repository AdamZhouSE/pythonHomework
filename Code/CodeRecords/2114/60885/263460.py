from math import sqrt

def count_from(num, base):
    count = 0
    while num > 0:
        b = base*base
        if num >= b:
            count += 1
            num -= b
        else:
            base -= 1
    return count

def count(num):
    base = int(sqrt(num))
    result = count_from(num, 1)
    for i in range(2, base+1):
        temp = count_from(num, i)
        if temp < result:
            result = temp
    return result

n = int(input())
result = count(n)
print(result)