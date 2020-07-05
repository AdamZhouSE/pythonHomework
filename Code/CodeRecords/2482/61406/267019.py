T = int(input())
for a in range(0,T):
    N = int(input())
    D = int(input())
    number = str(N//D)
    quotient = ""
    remainder = [N%D]
    while True:
        x,y=divmod(remainder[-1]*10,D)
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




