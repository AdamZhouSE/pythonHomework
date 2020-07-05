dividend=int(input())
divisor=int(input())
quotient=dividend//divisor
if(quotient<0):
    quotient+=1

print(quotient)