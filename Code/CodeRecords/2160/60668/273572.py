def nums_33_divide(dividend,divisor):
    co = []
    con = 0
    if(divisor>0 and dividend>0) :
        while sum(co)<dividend:
            co.append(divisor)
        con = len(co)
    elif divisor<0 and dividend<0:
        while sum(co)>dividend:
            co.append(divisor)
        con = len(co)
    elif divisor<0 and dividend>0:
        divisor = -divisor
        while sum(co)<dividend:
            co.append(divisor)
        con = -len(co)
    else:
        dividend = -dividend
        while sum(co)<dividend:
            co.append(divisor)
        con = len(co)
    return con
if __name__=='__main__':
    dividend = int(input())
    divisor = int(input())
    print(nums_33_divide(dividend,divisor))