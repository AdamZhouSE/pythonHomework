num1=input()
num2=input()
num1=num1[1:-1]
num2=num2[1:-1]
number1=[]
number2=[]
for x in num1:
    if x.isdigit():
        number1.append(int(x))
    else:
        continue
for y in num2:
    if y.isdigit():
        number2.append(int(y))
    else:
        continue
result=[value for value in number1 if value in number2]
result.sort()
print(result)