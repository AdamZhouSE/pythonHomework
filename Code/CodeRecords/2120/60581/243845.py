str = int(input())

maxNumber = 1

for i in range(1,str):
    exponent = int(str/i)
    if str%i == 1:
        exponent -= 1
    number = pow(i,exponent)*max((str-exponent*i),1)
    if number > maxNumber:
        maxNumber = number

print(maxNumber)