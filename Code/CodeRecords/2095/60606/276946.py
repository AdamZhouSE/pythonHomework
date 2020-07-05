a = input()
b = input()
operand1 = "0b"+a
operand2 = "0b"+b
result = int(operand1,2)+int(operand2,2)
print(bin(result)[2:])
