dividend = int(input())
divisor = int(input())
count = 0
while dividend >= divisor:
    dividend = dividend - divisor
    count = count + 1
print(count)