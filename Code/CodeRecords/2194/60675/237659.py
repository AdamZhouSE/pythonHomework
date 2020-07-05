numberOfEx = int(input())

def isNumber(num):
    if num <=1:
        return -1
    for i in range(2,int(num/2)+1):
        if num%i ==0:
            return num
    return 0

for i in range(0,numberOfEx):
    x = input()
    num = []
    value = ''
    for i in range(1, len(x) + 1):
        if x[i - 1] != " ":
            value = value + x[i - 1]
            continue
        else:
            num.append(value)
            value = ''
    num.append(value)
    value = ''

    lower = int(num[0])
    upper = int(num[1])
    output = ""
    for i in range(lower,upper+1):
        if isNumber(i)==0:
            output = output + str(i) + " "
    print(output.strip())