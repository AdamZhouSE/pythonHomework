num1 = float(input())
num2 = int(input())
flag_negative = False
result = float(1)
if num2 < 0:
    flag_negative = True
    num2 = -num2
if num1 == 0:
    print("invalid")
if num2 == 0:
    print(float(1))
for i in range(num2):
    result *= num1
print(format(result, '.5f'))
