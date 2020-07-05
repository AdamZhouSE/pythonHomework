def reflection1(x):
    if x=='1':
        return "One"
    elif x=='2':
        return "Two"
    elif x=='3':
        return "Three"
    elif x=='4':
        return "Four"
    elif x=='5':
        return "Five"
    elif x=='6':
        return "Six"
    elif x=='7':
        return "Seven"
    elif x=='8':
        return "Eight"
    elif x=='9':
        return "Nine"


def reflection2(x):
    result = ""
    if x[0]=='1':
        if x[1]=='1':
            return "Eleven"
        elif x[1]=='2':
            return "Twelve"
        elif x[1]=='3':
            return "Thirteen"
        elif x[1]=='4':
            return "Fourteen"
        elif x[1]=='5':
            return "Fifteen"
        elif x[1]=='6':
            return "Sixteen"
        elif x[1]=='7':
            return "Seventeen"
        elif x[1]=='8':
            return "Eighteen"
        elif x[1]=='9':
            return "Nineteen"
    elif x[0]=='2':
        result = "Twenty"
    elif x[0]=='3':
        result = "Thirty"
    elif x[0]=='4':
        result = "Forty"
    elif x[0]=='5':
        result = "Fifty"
    elif x[0]=='6':
        result = "Sixty"
    elif x[0]=='7':
        result = "Seventy"
    elif x[0]=='8':
        result = "Eighty"
    elif x[0]=='9':
        result = "Ninety"
    result = result + " " + reflection1(x[1])
    return result


def hundred(x):
    if len(x)==1:
        return reflection1(x)
    elif len(x)==2:
        return reflection2(x)
    else:
        return reflection1(x[0])+" Hundred " + reflection2(x[1:])


def thousand(x):
    return hundred(x[0:len(x)-3])+" Thousand "+hundred(x[len(x)-3:])


def million(x):
    return hundred(x[0:len(x)-6])+" Million "+thousand(x[len(x)-6:])


def billion(x):
    return hundred(x[0:len(x)-9])+" Billion "+million(x[len(x)-9:])


n = input()
result=""
if 1<=len(n)<=3:
    result = hundred(n)
elif 4<=len(n)<=6:
    result = thousand(n)
elif 7<=len(n)<=9:
    result = million(n)
elif 10<=len(n):
    result = billion(n)
print(result)

