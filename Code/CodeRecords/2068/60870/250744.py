dividend = int(input())
divisor = int(input())
control = ''
count = 0
if dividend < 0 and divisor > 0:
    control = '-'
    dividend = 0 - dividend
if dividend > 0 and divisor < 0:
    control = '-'
    divisor = 0 - divisor
while dividend >= divisor:
    dividend = dividend - divisor
    count = count + 1
print(control + str(count))