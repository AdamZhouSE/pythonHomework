def strToInteger(str1):
    result=0
    for i in range(0,len(str1)):
        result=result*10+int(str1[i])
    return result

num1=strToInteger(input())
num2=strToInteger(input())
product=num1*num2
print(str(product))