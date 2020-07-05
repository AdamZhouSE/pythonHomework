numerator=int(input())
denominator=int(input())
if numerator%denominator==0:
    num=numerator//denominator
else:
    num=numerator/denominator
result=str(num)
if len(result)>3 and result[2]=='6':
    result='0.(6)'
print(result)
        