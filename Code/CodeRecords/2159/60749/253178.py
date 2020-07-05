n=int(input())
def NumtoRoma(num):
    result=""
    dic1 = {1:'I',4:"IV", 5:'V', 9:"IX",10:'V', 40:"XL",50:'L',90:"XC", 100:'C',400:"CD",500:'D',900:"CM",1000:'M'}
    dic2={1:0,4:0, 5:0, 9:0,10:0, 40:0,50:0,90:0, 100:0,400:0,500:0,900:0,1000:0}
    dic2[1000]=num//1000
    result+=dic1[1000]*dic2[1000]
    num=num%1000
    dic2[900]=num//900
    result+=dic1[900]*dic2[900]
    num=num%900
    if num<100:
        dic2[90]=num//90
        result+=dic1[90]*dic2[90]
        num=num%90
        if num<10:
            result+=NumtoRomalessthan10(num)
        else:
            dic2[50]=num//50
            result+=dic1[50]*dic2[50]
            num=num%50
            result+=NumtoRomalessthan50(num)
    else:
        dic2[500]=num//500
        result+=dic1[500]*dic2[500]
        num=num%500
        dic2[100]=num//100
        result+=dic1[100]*dic2[100]
        num=num%100
        result+=NumtoRomalessthan100(num)
    return result

def NumtoRomalessthan100(num):
    result=""
    if num>=90:
        result+="CX"
        result+=NumtoRomalessthan10(num-90)
    else:
        if num<10:
            result+=NumtoRomalessthan10(num)
        else:
            result+="L"*(num//50)
            num=num%50
            result+=NumtoRomalessthan50(num)
    return result
def NumtoRomalessthan50(num):
    result=""
    if num>=40:
        result+="XL"
        result+=NumtoRomalessthan10(num-40)
    else:
        result+="X"*(num//10)
        num=num%10
        result+=NumtoRomalessthan10(num)
    return result

def NumtoRomalessthan10(num):
    result=""
    if num == 9:
        result += "IX"
    elif num >= 5:
        result += "V"
        result += "I" * (num - 5)
    elif num == 4:
        result += "IV"
    else:
        result += "I" * num
    return result
print(NumtoRoma(n))