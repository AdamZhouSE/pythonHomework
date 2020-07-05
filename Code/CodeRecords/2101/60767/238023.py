def isHappyNumber(num):
    sum = 0
    res = []
    for i in str(num):
        sum = sum + int(i)*int(i)
    res.append(sum)
    while(sum!=1):
        temp = sum
        sum = 0
        for x in str(temp):
            sum = sum + int(x)*int(x)
        if(sum==89):
            return False
        if(sum in res):
            return False
    return True

num = int(input())
print(isHappyNumber(num))