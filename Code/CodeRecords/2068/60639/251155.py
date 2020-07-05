import math
dividend=int(input())
divisor=int(input())
quotient=dividend/divisor
if quotient<0:
    print(math.ceil(quotient))
else:
    print(math.floor(quotient))