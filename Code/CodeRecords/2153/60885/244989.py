num = int(input())
result = 0
neg = num < 0
if neg:
    num = -num
while num > 0:
    result = result * 10 + num % 10
    num = int(num/10)
if neg:
    result = -result
print(result)