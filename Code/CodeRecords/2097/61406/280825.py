numerator = int(input())
denominator = int(input())
number = str(numerator//denominator)
quotient = ""
remainder = [numerator%denominator]
while True:
    x,y=divmod(remainder[-1]*10,denominator)
    quotient = quotient+str(x)
    remainder.append(y)
    i = remainder.index(remainder[-1])
    if i!= len(remainder)-1:
        quotient = quotient[:i]+"("+quotient[i:]+")"
        break
result = number+"."+quotient
if result.endswith("(0)"):
    result = result[:-3]
if result.endswith("."):
    result = result[:-1]
print(result)