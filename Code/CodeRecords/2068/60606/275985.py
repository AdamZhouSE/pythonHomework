import math
dividend = int(input())
divisor = int(input())
result = dividend/divisor
if result>0:
    print(math.floor(result))
else:
    print(math.ceil(result))