def conv(a):
    if a%26==0:
        return"Z"
    elif a%26==1:
        return"A"
    elif a%26==2:
        return"B"
    elif a%26==3:
        return"C"
    elif a%26==4:
        return"D"
    elif a%26==5:
        return"E"
    elif a%26==6:
        return"F"
    elif a%26==7:
        return"G"
    elif a%26==8:
        return"H"
    elif a%26==9:
        return"I"
    elif a%26==10:
        return"J"
    elif a%26==11:
        return"K"
    elif a%26==12:
        return"L"
    elif a%26==13:
        return"M"
    elif a%26==14:
        return"N"
    elif a%26==15:
        return"O"
    elif a%26==16:
        return"P"
    elif a%26==17:
        return"Q"
    elif a%26==18:
        return"R"
    elif a%26==19:
        return"S"
    elif a%26==20:
        return"T"
    elif a%26==21:
        return"U"
    elif a%26==22:
        return"V"
    elif a%26==23:
        return"W"
    elif a%26==24:
        return"X"
    else:
        return"Y"
n=int(input())
if n <=26:
    print(conv(n))
else:
    print(conv(n//26)+conv(n))