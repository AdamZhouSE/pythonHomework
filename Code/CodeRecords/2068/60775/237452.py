a = int(input())
b = int(input())
quotion = 0
dividend_neg = True if a<0 else False
remainder_neg = dividend_neg

if a == 0:
    print(0)

elif (a < 0 and b<0) or (a > 0 and b >0):
    while dividend_neg == remainder_neg:
        a = a-b
        quotion += 1
        remainder_neg = True if a<0 else False
    quotion -= 1

elif (a<0 and b>0) or (a>0 and b<0):
    while dividend_neg == remainder_neg:
        a = a+b
        quotion -= 1
        remainder_neg = True if a<0 else False
    quotion += 1
print(quotion)