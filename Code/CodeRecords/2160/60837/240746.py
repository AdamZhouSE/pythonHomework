def div(dividend,divisor):
    if dividend<0:
        return div(-dividend,-divisor)
    elif dividend==0:
        return 0
    else:
        res=0
        if divisor>0: 
            while dividend>=divisor:
                dividend-=divisor
                res+=1
        else:
            while dividend>=-divisor:
                dividend+=divisor
                res-=1
        return res

dividend=int(input())
divisor=int(input())
print(div(dividend,divisor))
        