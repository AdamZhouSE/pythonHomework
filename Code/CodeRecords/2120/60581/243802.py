str = int(input())

number1 = int(str/2)
number1 = number1 * (str-number1)

number2 = int(str/3)
number2 = number2 * number2 * (str-2*number2)

print(max(number1,number2))