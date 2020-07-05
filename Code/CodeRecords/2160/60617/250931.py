def div():
    dividend=int(input())
    divisor=int(input())
    sign=""
    if (dividend>0 and divisor<0) or (dividend<0 and divisor>0):
        sign="-"
    dividend=abs(dividend)
    divisor=abs(divisor)
    quotient=0
    while dividend-divisor>=0:
        dividend=dividend-divisor
        quotient+=1
    print(sign+str(quotient))
    
if __name__=='__main__':
    div()
