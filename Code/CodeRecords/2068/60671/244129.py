dividend=int(input())
divisor=int(input())
quotient=0
while(dividend>0):
    dividend-=divisor
    quotient+=1

print(quotient)