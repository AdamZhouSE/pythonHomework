

def divide(dividend,divisor):
    if dividend==0: return 0
    neg=False
    if dividend*divisor<0: neg=True
    if dividend<0: dividend=-dividend
    if divisor<0: divisor =-divisor
    cnt=-1
    while dividend>0:
        cnt+=1
        dividend-=divisor
    if neg: cnt=-cnt
    return cnt
print(divide(int(input()),int(input())))