def over(num):
    result = 0
    while num > 0:
        result *= 10
        result += num%10
        num = int(num/10)
    return result
        
num = int(input())

if num < 10 and num >= 0:
    print(num)
elif num < 0:
    print(-1*over(-1*num))
else:
    print(over(num))