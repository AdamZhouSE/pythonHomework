str = int(input())

maxNumber = 1

for i in range(1,str):
    exponent = int(str/i)
    number = pow(i,exponent)*(str-exponent*i)
    if number > maxNumber:
        maxNumber = number

print(maxNumber)