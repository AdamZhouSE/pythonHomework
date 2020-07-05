def isNumber(num):
    if num <=1:
        return False
    for i in range(2,int(num/2)+1):
        if num%i ==0:
            return False
    return True

def isNum(num):
    n = 0
    while num !=0:
        q = num %2
        num = int(num/2)
        if q == 1:
            n +=1
    if isNumber(n):
        return True
    else:
        return False


n = input()
number = int(n)

for i in range(1,number+1):
    a = input()
    list = a.split()
    lower = int(list[0])
    upper = int(list[1])
    numOfAnswer = 0
    for j in range(lower,upper+1):
        if isNum(j):
            numOfAnswer +=1
    print(numOfAnswer)
