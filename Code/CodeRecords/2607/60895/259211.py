t=int(input())
while t>0:
    t=t-1
    s=input()
    print(s)
    length=len(s)
    least=3
    result=0
    while least<length:
        for i in range(0,length-least):
            temp=s[i:i+least]
            set1=set(temp)
            if set1=={'0','1','2'}:
                num0=0
                num1=0
                num2=0
                for item in temp:
                    if item=='0':
                        num0=num0+1
                    elif item=='1':
                        num1=num1+1
                    else:
                        num2=num2+1
                if num0!=1 or num1!=1:
                    break
                for j in range(i+1,length-least+1):
                    compare=s[j:j+least]
                    set2=set(compare)
                    if set2=={'0','1','2'}:
                        num3=0
                        num4=0
                        num5=0
                        for item in compare:
                            if item=='0':
                                num3=num3+1
                            elif item=='1':
                                num4=num4+1
                            else:
                                num5=num5+1
                        if num3==1 and num4==1 and num5==num2:
                            result=result+1
                            break
        least=least+1
    print(result)              