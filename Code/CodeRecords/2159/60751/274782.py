num=input()
a=0
result=""
for i in range(len(num)):
    a+=1
    val=int(num[len(num)-i-1])
    if a==1:
        if val<4:
            result+="I"*val
        elif val==4:
            result+="IV"
        elif 9>val>=5:
            result+="V"+"I"*(val-5)
        else:
            result+="IX"
    if a==2:
        if val<4:
            result="X"*val+result
        elif val==4:
            result="XL"+result
        elif 9>val>=5:
            result="L"+"X"*(val-5)+result
        else:
            result="XC"+result
    if a==3:
        if val<4:
            result="C"*val+result
        elif val==4:
            result="CD"+result
        elif 9>val>=5:
            result="D"+"C"*(val-5)+result
        else:
            result="CM"+result
    if a==4:
        result="M"*val+result
print(result)
    