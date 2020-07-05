dividend = int(input())
divisor = int(input())
if dividend*divisor < 0:
    print(dividend//divisor+1)
else:
    print(dividend//divisor)