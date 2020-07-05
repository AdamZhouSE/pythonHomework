num1 = list(input())[::-1]
num2 = list(input())[::-1]
result = ['0' for i in range(len(num1 + num2))]
for i in range(len(num1)):
    for j in range(len(num2)):
        temp = int(num1[i]) * int(num2[j])
        if temp >= 10:
            result[i+j+1] = str(int(result[i+j+1]) + int(temp/10))
            temp = temp % 10
        result[i+j] = str(int(result[i+j]) + temp)
        for k in range(len(result)):
            if len(result[k]) == 2:
                result[k+1] = str(int(result[k+1]) + int(int(result[k])/10))
                result[k] = str(int(int(result[k])%10))
result = ''.join(result[::-1]).lstrip('0')
print(result)