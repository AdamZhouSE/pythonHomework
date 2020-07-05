def change(num):
    res=""
    th=num//1000
    num=num%1000
    hun=num//100
    num=num%100
    ten=num//10
    one=num%10
    res=res+"M"*th
    if hun==9:
        res+="CM"
    elif hun>=5:
        res+="D"+"C"*(hun-5)
    elif hun==4:
        res+="CD"
    else:
        res+="C"*hun


    if ten==9:
        res+="XC"
    elif ten>=5:
        res+="L"+"X"*(ten-5)
    elif ten==4:
        res+="XL"
    else:
        res+="X"*ten


    if one==9:
        res+="IX"
    elif one>=5:
        res+="V"+"I"*(one-5)
    elif one==4:
        res+="IV"
    else:
        res+="I"*one
    return res
num=int(input())
print(change(num))