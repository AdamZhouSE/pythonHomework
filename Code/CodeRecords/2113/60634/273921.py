oneList = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Evelen", "Twelve",
           "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "eighteen", "nineteen"]
tenList = ["Zero", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety", "Hundred"]

def threeBit(num,i,result,str):
    count = 0
    temp = ""
    while i >= 0 and count < 3:
        temp = num[i] + temp
        count += 1
        i -= 1
    result = hundTran(temp) + str  + result
    return [count,result]

def smallTran(num):
    if len(num) == 1:
        return oneList[int(num)]
    elif len(num) == 2:
        n = int(num)
        if num[0] == '0':
            return oneList[int(num)]
        if n < 20:
            return oneList[n]
        else:
            if n % 10 == 0:
                return tenList[int(n / 10)]
            else:
                return tenList[int(num[0])] + " " + oneList[int(num[1])]

def hundTran(num):
    if len(num) <= 2:
        return smallTran(num)
    n = int(num[0])
    if n == 0:
        return smallTran(num[1:3])
    else:
        return oneList[n] + " " + tenList[10] + " " + smallTran(num[1:3])

def transform(num):
    result = ""
    i = len(num)-1

    temp = threeBit(num,i,result,"")
    i -= temp[0]
    result = temp[1]

    if i >= 0:
        temp = threeBit(num, i, result, " Thousand ")
        i -= temp[0]
        result = temp[1]

    if i >= 0:
        temp = threeBit(num, i, result, " Million ")
        i -= temp[0]
        result = temp[1]

    if i >= 0:
        temp = threeBit(num, i, result, " Billion ")
        i -= temp[0]
        result = temp[1]

    return result

# main-----
str = input()
print(transform(str))