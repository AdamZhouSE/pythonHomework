def fx(num1,num2):
    re= []
    for i in range(0, len(num1)):
        for j in range(0, len(num2)):
            if num1[i] == num2[j]:
                re.append(num2[j])
                num2[j] = -1
                break
    re.sort()
    return re
num1=eval(input())
num2=eval(input())
result=[]
result=fx(num1,num2)
print(result)