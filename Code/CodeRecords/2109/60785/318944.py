def addDigits(num):
    sum = hanshu(num)
    while (sum >= 10):
        sum = hanshu(sum)
    return sum
def hanshu(num):
    sum = 0
    while (num> 0):
        ge = num % 10
        sum += ge
        num = int(num / 10)
    return sum
num=int(input())
print(addDigits(num))