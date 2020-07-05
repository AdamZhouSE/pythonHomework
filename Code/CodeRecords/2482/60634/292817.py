def exist(ch,list):
    i = 0
    while i < len(list):
        if ch == list[i]:
            return i
        i += 1
    return -1


def div(num,den):
    resList = []
    sList = []
    result = ""
    
    s = int(num/den)
    res = num % den
    if res == 0:
        return str(s)
    
    result += str(s) + "."
    
    while True:
        num = res * 10
        s = int(num/den)
        sList.append(str(s))
        res = num % den 
        if res == 0:
            for c in sList:
                result += c
            return result
        temp = exist(res,resList)
        if temp == -1:
            resList.append(res)
        else:
            result += "("
            while temp < len(sList)-1:
                result += sList[temp]
                temp += 1
            result += ")"
            return result


#main-----
test = int(input())
for t in range(test):
    num = int(input())
    den = int(input())
    print(div(num,den))























