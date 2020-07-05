dividend = int(input())
divisor = int(input())
neg = False
count = 0
if dividend > 0 > divisor:
    neg = True
    divisor = - divisor
elif dividend < 0 < divisor:
    neg = True
    dividend = -dividend
while dividend-divisor > 0:
    dividend -= divisor
    count += 1
if neg:
    count =-count
print(count)